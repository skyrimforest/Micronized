from RMQ import rmq_send,rmq_recv
import time
import json
import numpy as np
from .FaceDetection import FaceDetection
from SkyLogger import get_logger
import requests
from API import dispatcher_api
logger = get_logger("tasks")

args = {
    'net_type': 'mb_tiny_RFB_fd',
    'input_size': 480,
    'threshold': 0.7,
    'candidate_size': 1500,
    'device': 'cuda:0',
}
face_detection = FaceDetection(args)
# 接收图片之后发送图片
# 图片格式为:
# image_info = {
# 'uuid': uid,
# 'image_name': file,
# 'image_mat': image.tolist(),
# }
# cnt用于记录图片数量
cnt=0
def my_callback(ch, method, properties, body):
    start = time.time()
    body = body.decode()
    # packet is wrong then drop it
    try:
        body = json.loads(body)
    except:
        ch.basic_ack(delivery_tag=method.delivery_tag)
        return
    image=np.array(body['image_mat'],dtype=np.uint8)
    image_name=body['image_name']
    print(f"{image_name} has been received")
    boxes, labels, probs = face_detection(image)
    image_info = {
        'uuid': body['uuid'],
        'image_name': image_name,
        'image_mat': image.tolist(),
        'boxes': boxes.tolist(),
    }
    # 发送给下一阶段流水线
    rmq_send(image_info)
    global cnt
    cnt+=1
    ch.basic_ack(delivery_tag=method.delivery_tag)
    end = time.time()
    logger.info(f"send_task down,{cnt} images have been processed,{end-start} second used")


    data={
        "uuid":body['uuid'],
        "count": cnt,
        "image_name": image_name,
        "detected": len(boxes),
        "total_time":end-start
    }

    res=requests.post(dispatcher_api.API['detectinfo'],json=data)
    logger.info(f"collected down,result is {res.text}")

