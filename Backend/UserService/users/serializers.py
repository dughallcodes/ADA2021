from django.db import models
from django.db.models import fields
from users.models import Courier, User, Address
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
import logging


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        exclude = ("id",)


class CourierSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        required=True, validators=[UniqueValidator(queryset=Courier.objects.all())]
    )
    email = serializers.EmailField(
        required=True, validators=[UniqueValidator(queryset=Courier.objects.all())]
    )
    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = Courier
        exclude = ("id",)


class UserSerializer(serializers.ModelSerializer):
    address = AddressSerializer(many=False, required=False)
    username = serializers.CharField(
        required=True, validators=[UniqueValidator(queryset=User.objects.all())]
    )
    email = serializers.EmailField(
        required=True, validators=[UniqueValidator(queryset=User.objects.all())]
    )
    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        depth = 1
        exclude = ("id",)

    def create(self, validated_data):
        address_data = dict(validated_data.pop("address"))
        address = Address.objects.create(**address_data)
        user = User.objects.create(address=address, **validated_data)
        return user


class UserAddressSerializer(serializers.ModelSerializer):
    address = AddressSerializer(many=False, required=False)

    class Meta:
        model = User
        depth = 1
        fields = ("address",)