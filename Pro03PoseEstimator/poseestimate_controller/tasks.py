import BaseConfig
from RMQ import rmq_send,rmq_recv
import time
import json
import numpy as np
from SkyLogger import get_logger
from poseestimate_controller.FaceAlignment import FaceAlignmentCNN,draw_axis
import torch
import cv2

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
    body = json.loads(body)
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
    cv2.imwrite(BaseConfig.LOG_PATH + '/' + image_name, image)
    logger.info('pic results written!')

    global cnt
    cnt += 1
    ch.basic_ack(delivery_tag=method.delivery_tag)
    end = time.time()
    logger.info(f"draw down,{cnt} images have been drawed,{end - start} second used")

def recv_draw():
    logger.info("get pics and draw it")
    rmq_recv(my_draw_callback)



