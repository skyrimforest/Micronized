from fastapi import APIRouter,BackgroundTasks
from fastapi.responses import FileResponse
import time
import requests
import numpy as np
import torch
import cv2

import BaseConfig
from .FaceAlignment import FaceAlignmentCNN,draw_axis
from schema import *
from SkyLogger import get_logger
from API import dispatcher_api

logger = get_logger("estimate")

args = {
        'lite_version': False,
        'model': 'hopenet',
        'batch_size': 1,
        'device': 'cuda:0',
    }
face_alignment=FaceAlignmentCNN(args)

# 接收图片之后发送图片
# 图片格式为:
# image_info = {
#     'uuid':uid,
#     'image_name': image_name,
#     'image_mat': image.tolist(),
#     'boxes': boxes.tolist(),
# }
cnt=0
def recv_draw(detect_res:DetectRes):
    logger.info("get pics and draw it")
    start = time.time()
    body = detect_res.dict()
    try:
        image = np.array(body['image_mat'], dtype=np.uint8)
        image_name = body['image_name']
        boxes = torch.Tensor(body['boxes'])
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
                # cv2.putText(image,str(learning),(int(ax[0]), int(ax[1])),cv2.FONT_HERSHEY_PLAIN,1,(255,255,0),2)
        # print(learning)
        # cv2.putText(image,str(ax[8]),(int(ax[0]), int(ax[1])),cv2.FONT_HERSHEY_SIMPLEX,fontScale=0.5,color=(0,255,0),thickness=2)
        image_name = image_name.split('/')[-1]
        print(BaseConfig.OUTPUT_PATH + '/' + image_name)
        cv2.imwrite(BaseConfig.OUTPUT_PATH + '/' + image_name, image)
        logger.info('pic results written!')
    except:
        return

    global cnt
    cnt += 1
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
    # push log to db
    res = requests.post(dispatcher_api.API['estimateinfo'], json=data)

    end_time_info = {
        'uuid': body['uuid'],  # 运行次数标识符,系统一次运行只接受一种uuid
        'count': cnt,
        'image_name': image_name
    }
    # push end time to db
    requests.post(dispatcher_api.API['endtime'], json=end_time_info)
    logger.info(f"collected down,result is {res.text}")
    cnt=0


router = APIRouter(
    prefix="/estimate",
    tags=["estimate"],
    responses={404: {"description": "Not found"}},
)

@router.post("/test")
async def estimatetest():
    logger.info("poseestimate test success")
    return {"message": "poseestimate test success"}

@router.post("/draw")
async def drawaxis(detect_res:DetectRes,background_tasks: BackgroundTasks):
    background_tasks.add_task(recv_draw,detect_res)
    return {"message": "poseestimate test success"}

@router.get("/result/{name}")
async def get_pic_result(name: str):
    image_path=BaseConfig.LOG_PATH+'/'+name
    return FileResponse(image_path, media_type="image/jpeg")

