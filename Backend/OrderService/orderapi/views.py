from django.shortcuts import render
from rest_framework import viewsets
from .models import Location, Client, Order
from .serializer import LocationSerializer, ClientSerializer, OrderSerializer

# Create your views here.


class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer