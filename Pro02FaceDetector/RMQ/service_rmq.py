import pika
import BaseConfig
from typing import Dict
import json

credentials = pika.PlainCredentials(BaseConfig.RMQ_USER, BaseConfig.RMQ_PASS)

conn = pika.BlockingConnection(pika.ConnectionParameters(host=BaseConfig.RMQ_IP, port=BaseConfig.RMQ_PORT, virtual_host="/",
                              credentials=credentials,heartbeat=10))
channel = conn.channel()

def rmq_send(message:Dict[str, str]) -> None:
    message=json.dumps(message)

    channel.queue_declare(queue=BaseConfig.RMQ_QUEUE_FORWARD)
    channel.basic_publish(exchange='',
                          routing_key=BaseConfig.RMQ_QUEUE_FORWARD,
                          body=message,
                          properties=pika.BasicProperties(delivery_mode=pika.DeliveryMode.Persistent))

def rmq_recv(special_callback) -> None:
    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(queue=BaseConfig.RMQ_QUEUE_RECV, on_message_callback=special_callback)
    channel.start_consuming()

