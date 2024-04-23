from fastapi import APIRouter,BackgroundTasks
from fastapi.responses import FileResponse
import time
import requests
import numpy as np
import torch
import cv2

import BaseConfig
from poseestimate_controller.FaceAlignment import FaceAlignmentCNN,draw_axis
from schema import *
from SkyLogger import get_logger
from API import dispatcher_api
from poseestimate_controller.gender_classification import GenderClassification


logger = get_logger("estimate")


# 接收图片之后发送图片
# 图片格式为:cnt=0
# # 避免一开始就初始化模型
# def init_model():
#     global args
#     face_alignment = FaceAlignmentCNN(args)
#     logger.info("model initialized success")
#     return face_alignment
# image_info = {
#     'uuid':uid,
#     'image_name': image_name,
#     'image_mat': image.tolist(),
#     'boxes': boxes.tolist(),
# }
def init_model():
    global all_config
    args = {
        'lite_version': False,
        'model': 'hopenet',
        'batch_size': 1,
        'device': 'cuda:0',
    }
    face_estimator = FaceAlignmentCNN(args)
    logger.info("model initialized success")
    return face_estimator
def recv_draw(detect_res:DetectRes,face_alignment):
    start = time.time()
    body = detect_res.dict()
    image = np.array(body['image_mat'], dtype=np.uint8)
    image_name = body['image_name']
    boxes = torch.Tensor(body['boxes'])
    cnt=body['count']
    learning = 0
    # will return all people's info
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
                 (255, 0, 0), 2)
        if ax[7] <= ax[1]:
            learning += 1
    # image_name = image_name.split('/')[-1]
    cv2.imwrite(BaseConfig.OUTPUT_PATH + '/' + image_name, image)
    logger.info('pic results written!')
    end = time.time()
    logger.info(f"draw down,{cnt} images have been drawed,{end - start} second used")
    data = {
        "uuid": body['uuid'],
        "count": cnt,
        'image_name': image_name,
        'detected': len(head_pose),
        'learning': learning,
        "total_time": end - start,
    }
    # 记录estimate阶段的信息
    res = requests.post(dispatcher_api.API['estimateinfo'], json=data)

    end_time_info = {
        'uuid': body['uuid'],  # 运行次数标识符,系统一次运行只接受一种uuid
        'count': cnt,
        'image_name': image_name
    }
    # 记录系统结束时间
    requests.post(dispatcher_api.API['endtime'], json=end_time_info)
    logger.info(f"collected down,result is {res.text}")

router = APIRouter(
    prefix="/estimate",
    tags=["estimate"],
    responses={404: {"description": "Not found"}},
)

@router.post("/test")
async def estimatetest():
    logger.info("poseestimate test success")
    return {"message": "poseestimate test success"}


face_alignment=init_model()
@router.post("/draw")
async def drawaxis(detect_res:DetectRes,background_tasks: BackgroundTasks):
    background_tasks.add_task(recv_draw,detect_res,face_alignment)
    return {"message": "poseestimate test success"}

@router.get("/result/{name}")
async def get_pic_result(name: str):
    image_path=BaseConfig.LOG_PATH+'/'+name
    return FileResponse(image_path, media_type="image/jpeg")
