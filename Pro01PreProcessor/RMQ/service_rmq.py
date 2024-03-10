import pika
import BaseConfig
from typing import Dict
import json

# 登录
credentials = pika.PlainCredentials(BaseConfig.RMQ_USER, BaseConfig.RMQ_PASS)

conn = pika.BlockingConnection(
    pika.ConnectionParameters(host=BaseConfig.RMQ_IP, port=BaseConfig.RMQ_PORT, virtual_host="/",
                              credentials=credentials))
channel = conn.channel()

# 发送
def rmq_send(message:Dict[str, str]) -> None:
    # with lock:
    message=json.dumps(message)
    channel.queue_declare(queue=BaseConfig.RMQ_QUEUE)
    channel.basic_publish(exchange='',
                          routing_key=BaseConfig.RMQ_QUEUE,
                          body=message,
                          properties=pika.BasicProperties(delivery_mode=pika.DeliveryMode.Persistent))

# 接收
def rmq_recv(special_callback) -> None:
    # with lock:
    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(queue=BaseConfig.RMQ_QUEUE, on_message_callback=special_callback)
    channel.start_consuming()