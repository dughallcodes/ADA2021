import logging
from django.http import request
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework_simplejwt.authentication import JWTTokenUserAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
import pika
import json

# Create your views here.


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


def try_to_connect_to_channel():
    channel = None
    try:
        channel = attempt_connection()
    except pika.exceptions.AMQPChannelError as err:
        print("Caught a channel error: {}, stopping...".format(err))
        channel = attempt_connection()
    except pika.exceptions.AMQPConnectionError:
        print("Connection was closed, retrying...")
        channel = attempt_connection()
    return channel


class CourierAPI(viewsets.ViewSet):
    authentication_classes = [JWTTokenUserAuthentication]
    permission_classes = [IsAuthenticated]

    @action(detail=False, methods=["GET"])
    def accept_order(self, request):
        order_id = request.query_params["order_id"]
        courier_id = request.user.id
        logging.warning(request.auth)
        body = {
            "message": "order_assigned",
            "order_id": order_id,
            "courier_id": courier_id,
        }
        channel = try_to_connect_to_channel()
        if channel:
            channel.basic_publish(
                exchange="", routing_key="order_queue", body=json.dumps(body)
            )
            channel.close()
            return Response(status=200, data="Order accepted!")
        else:
            return Response(status=500, data="RabbitMQ is trolling")

    @action(detail=False, methods=["GET"])
    def pick_up_order(self, request):
        order_id = request.query_params["order_id"]
        courier_id = request.user.id
        logging.warning(request.auth)
        body = {
            "message": "order_picked_up",
            "order_id": order_id,
            "courier_id": courier_id,
        }
        channel = try_to_connect_to_channel()
        if channel:
            channel.basic_publish(
                exchange="", routing_key="order_queue", body=json.dumps(body)
            )
            channel.close()
            return Response(status=200, data="Order picked up")
        else:
            return Response(status=500, data="RabbitMQ is trolling")

    @action(detail=False, methods=["GET"])
    def deliver_order(self, request):
        order_id = request.query_params["order_id"]
        courier_id = request.user.id
        logging.warning(request.auth)
        body = {
            "message": "order_delivered",
            "order_id": order_id,
            "courier_id": courier_id,
        }
        channel = try_to_connect_to_channel()
        if channel:
            channel.basic_publish(
                exchange="", routing_key="order_queue", body=json.dumps(body)
            )
            channel.close()
            return Response(status=200, data="Order delivered")
        else:
            return Response(status=500, data="RabbitMQ is trolling")
