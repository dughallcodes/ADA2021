from django.contrib.auth.models import User, Group
from django.db.models import fields
from rest_framework import serializers
from .models import Location, Client, Order
from orderapi import models


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ["lat", "lng", "description"]

    def create(self, validated_data):
        return Location.objects.create(**validated_data)


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ["name", "location", "phone_number"]

    def create(self, validated_data):
        return Client.objects.create(**validated_data)


class OrderSerializer(serializers.ModelSerializer):
    client = serializers.PrimaryKeyRelatedField(queryset=Client.objects.all())
    pick_up_location = LocationSerializer()

    class Meta:
        model = Order
        fields = [
            "timestamp",
            "status",
            "client",
            "order_txt",
            "pick_up_location",
            "pick_up_description",
        ]

    def create(self, validated_data):
        pick_up_location_data = validated_data.pop("pick_up_location")
        order = Order.objects.create(**validated_data)
        loc = Location.objects.create(**pick_up_location_data)
        order.pick_up_location = loc
        return order
