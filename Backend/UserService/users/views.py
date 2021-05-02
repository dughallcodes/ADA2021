from django.shortcuts import render
from rest_framework import viewsets
from .models import User, Courier
from .serializers import UserSerializer, CourierSerializer
from rest_framework.response import Response


class CourierViewSet(viewsets.ModelViewSet):
    queryset = Courier.objects.all()
    serializer_class = CourierSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
