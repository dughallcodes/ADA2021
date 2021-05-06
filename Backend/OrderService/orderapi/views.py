from re import I
from django.shortcuts import render
from rest_framework import viewsets
from .models import Order
from .serializer import OrderSerializer
from rest_framework_simplejwt.authentication import JWTTokenUserAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
import logging


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
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
