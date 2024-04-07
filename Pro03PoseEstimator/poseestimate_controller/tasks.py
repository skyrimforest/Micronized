import requests

import BaseConfig
from RMQ import rmq_send,rmq_recv
import time
import json
import numpy as np
from SkyLogger import get_logger
from poseestimate_controller.FaceAlignment import FaceAlignmentCNN,draw_axis
import torch
import cv2
from API import dispatcher_api

logger = get_logger("tasks")

args = {
    'lite_version': False,
    'model': 'hopenet',
    'batch_size': 1,
    'device': 'cuda:0',
}
face_alignment = FaceAlignmentCNN(args)

# 接收图片之后发送图片
# 图片格式为:
# image_info = {
#     'uuid':uid,
#     'image_name': image_name,
#     'image_mat': image.tolist(),
#     'boxes': boxes.tolist(),
# }
def my_callback(ch, method, properties, body):
    start = time.time()
    body = body.decode()
    body = json.loads(body)
    image=np.array(body['image_mat'],dtype=np.uint8)
    image_name=body['image_name']
    boxes=torch.Tensor(body['boxes'])

    head_pose = face_alignment(image, boxes)
    global cnt
    cnt+=1
    ch.basic_ack(delivery_tag=method.delivery_tag)
    end = time.time()
    logger.info(f"send_task down,{cnt} images have been processed,{end-start} second used")

cnt=0

def recv_forward_task():
    logger.info("recv_task start")
    rmq_recv(my_callback)

# 用户绘图的回调函数
def my_draw_callback(ch, method, properties, body):
    start = time.time()
    body = body.decode()
    try:
        body = json.loads(body)
    except:
        ch.basic_ack(delivery_tag=method.delivery_tag)
        return
    image = np.array(body['image_mat'], dtype=np.uint8)
    image_name = body['image_name']
    boxes = torch.Tensor(body['boxes'])

    head_pose = face_alignment(image, boxes)
    axis = []
    for yaw, pitch, roll, tdx, tdy, size in head_pose:
        ax = draw_axis(image, yaw, pitch, roll, tdx=tdx, tdy=tdy, size=size)
        axis.append(ax)

    for ax in axis:
        cv2.line(image, (int(ax[0]), int(ax[1])), (int(ax[2]), int(ax[3])),
                 (0, 0, 255), 3)
        cv2.line(image, (int(ax[0]), int(ax[1])), (int(ax[4]), int(ax[5])),
                 (0, 255, 0), 3)
        cv2.line(image, (int(ax[0]), int(ax[1])), (int(ax[6]), int(ax[7])),
                 (0, 255, 255), 2)

    # image_name='test'
    # print(image_name)
    # cv2.imshow('image', image)
    # cv2.waitKey(1)
    image_name=image_name.split('/')[-1]
    print(BaseConfig.OUT_PATH + '/' + image_name)
    cv2.imwrite(BaseConfig.OUT_PATH + '/' + image_name, image)
    logger.info('pic results written!')

    global cnt
    cnt += 1
    ch.basic_ack(delivery_tag=method.delivery_tag)
    end = time.time()
    logger.info(f"draw down,{cnt} images have been drawed,{end - start} second used")
    data={
        "uuid":body['uuid'],
        "count": cnt,
        'image_name':image_name,
        'detected':len(head_pose),
        'learning':len(head_pose), #todo
        "total_time":end-start,
    }
    # push log to db
    res=requests.post(dispatcher_api.API['estimateinfo'],json=data)

    end_time_info={
        'uuid': body['uuid'],  # 运行次数标识符,系统一次运行只接受一种uuid
        'count': cnt,
        'image_name': image_name
    }
    # push end time to db
    requests.post(dispatcher_api.API['endtime'],json=end_time_info)
    logger.info(f"collected down,result is {res.text}")

def recv_draw():
    logger.info("get pics and draw it")
    rmq_recv(my_draw_callback)




