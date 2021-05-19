from django.db.models import fields
from rest_framework import serializers
from .models import Address, Order


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        exclude = ("id",)


class OrderSerializer(serializers.ModelSerializer):
    pick_up_location = AddressSerializer(many=False, required=True)
    delivery_location = AddressSerializer(many=False, required=True)

    class Meta:
        model = Order
        depth = 1
        fields = "__all__"

    def create(self, validated_data):
        pick_up_location_data = dict(validated_data.pop("pick_up_location"))
        pick_up_location = Address.objects.create(**pick_up_location_data)
        delivery_location_data = dict(validated_data.pop("delivery_location"))
        delivery_location = Address.objects.create(**delivery_location_data)
        order = Order.objects.create(
            pick_up_location=pick_up_location,
            delivery_location=delivery_location,
            **validated_data
        )
        return order