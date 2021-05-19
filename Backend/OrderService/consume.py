from django.conf import settings
import django
import os
import pika
import json
import logging
import uuid

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
django.setup()


from orderapi.models import Order

connection = pika.BlockingConnection(
    pika.ConnectionParameters(
        host="rabbitmq",
        virtual_host="/",
        credentials=pika.PlainCredentials(username="rabbitmq", password="rabbitmq"),
    )
)
channel = connection.channel()

channel.queue_declare(queue="order_queue")


def callback(ch, method, properties, body):
    message = json.loads(body.decode())
    if message["message"] == "order_assigned":
        Order.objects.filter(id=message["order_id"]).update(
            status="ASSIGNED", courier_id=message["courier_id"]
        )

    if message["message"] == "order_picked_up":
        Order.objects.filter(id=message["order_id"]).update(
            status="PICKUP", courier_id=message["courier_id"]
        )

    if message["message"] == "order_delivered":
        Order.objects.filter(id=message["order_id"]).update(
            status="COMPLETED", courier_id=message["courier_id"]
        )


channel.basic_consume(queue="order_queue", on_message_callback=callback, auto_ack=True)

print(" [*] Waiting for messages. To exit press CTRL+C")
channel.start_consuming()