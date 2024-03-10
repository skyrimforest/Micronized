from celery import Celery
from celery.result import AsyncResult
from kombu import Queue ,Exchange
import BaseConfig
# class Config(object):
#     BROKER_URL='pyamqp://skyrim:111111@192.168.227.129//'
#     CELERY_QUEUES = (
#         Queue(
#             BaseConfig.RMQ_QUEUE+'test',
#             exchange=Exchange(''),
#             routing_key=BaseConfig.RMQ_QUEUE+'test',
#             queue_arguments={'x-max-length': 10}
#         ),
#     )
#broker中是用户名:密码@ip/vhost的格式
celery_app = Celery('preprocess_celery',
             broker='pyamqp://skyrim:111111@192.168.227.129//',
             backend='rpc://',
             include=['preprocess_controller.tasks'])

celery_app.conf.task_default_queue = 'default'

celery_app.conf.task_queues = (
    Queue(
        'default',
        exchange=Exchange('default'),
        routing_key='default',
        queue_arguments={'x-max-length': 5}  # 设置队列的最大长度为 1000
    ),
)


def get_task_info(task_id):
    """返回给定task_id的任务信息"""
    task_result = AsyncResult(task_id)
    result = {
        "task_id": task_id,
        "task_status": task_result.status,
        "task_result": task_result.result
    }
    return result

