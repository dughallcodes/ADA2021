from django.shortcuts import render
from rest_framework import viewsets
from .models import BasicUser, Address
from .serializers import BasicUserSerializer, AddressSerializer


class BasicUserViewSet(viewsets.ModelViewSet):
    queryset = BasicUser.objects.all()
    serializer_class = BasicUserSerializer
