import json
from re import I
from django.shortcuts import render
from pika import channel, connection
from rest_framework import viewsets
from .models import Order, Address
from .serializer import OrderSerializer
from rest_framework_simplejwt.authentication import JWTTokenUserAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action, permission_classes
from rest_framework import status
import pika
from json import dumps
import logging


def attempt_connection():
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(
            host="rabbitmq",
            virtual_host="/",
            credentials=pika.PlainCredentials(username="rabbitmq", password="rabbitmq"),
        )
    )
    channel = connection.channel()
    channel.queue_declare(queue="order_queue")
    return channel


channel = None
try:
    channel = attempt_connection()
except pika.exceptions.AMQPChannelError as err:
    print("Caught a channel error: {}, stopping...".format(err))
    channel = attempt_connection()
# Recover on all other connection errors
except pika.exceptions.AMQPConnectionError:
    print("Connection was closed, retrying...")
    channel = attempt_connection()


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    authentication_classes = [
        JWTTokenUserAuthentication,
    ]
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        request_data = request.data
        data = {**request_data, "client_id": request.user.id}
        serializer = OrderSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            body = {"message": "order_created", **serializer.data}
            channel.basic_publish(
                exchange="", routing_key="order_queue", body=json.dumps(body)
            )
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False)
    def get_order_by_user_id(self, request):
        user_id = request.query_params.get("user_id")
        orders_by_user = Order.objects.filter(client_id=user_id)
        if orders_by_user is not None:
            serializer = self.get_serializer(orders_by_user, many=True)
            return Response(status=200, data=serializer.data)
        return Response(status=404, data=None)

    @action(detail=True)
    def cancel_order(self, request, pk=None):
        order = Order.objects.get(id=pk)
        if not order:
            return Response(status=404)
        if order.status == "INIT":
            order.status = "CANCELED"
            order.save()
            body = {"message": "order_canceled", "order_id": str(order.id)}
            channel.basic_publish(
                exchange="", routing_key="order_queue", body=json.dumps(body)
            )
            return Response(status=200, data={"message": "Order canceled!"})
        else:
            return Response(
                status=401,
                data={
                    "message": f"Order's status is {order.status} so it can't be canceled!"
                },
            )

    @action(detail=False)
    def get_available_orders(self, request):
        orders = Order.objects.filter(status="INIT").values()
        for order in orders:
            print(order)
            order["pick_up_location"] = Address.objects.filter(
                id=order["pick_up_location_id"]
            ).values()
            order["delivery_location"] = Address.objects.filter(
                id=order["delivery_location_id"]
            ).values()
        return Response(status=200, data=orders)