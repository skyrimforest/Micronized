import requests

import BaseConfig
from RMQ import rmq_send
import os
import time
import cv2
from SkyLogger import get_logger
import uuid
from API import dispatcher_api


logger = get_logger("tasks")

def sendpics_task(picsfilePath:str):
    logger.info("sendpics_task start")
    start_time = time.time()
    cnt=0
    uid=str(uuid.uuid4())
    for root, dirs, files in os.walk(picsfilePath):
        for file in files:
            cnt+=1
            file_path = picsfilePath + '/' + file
            image = cv2.imread(file_path)
            image_info = {
                'uuid': uid, #运行次数标识符,系统一次运行只接受一种uuid
                'image_name': file, # 图片文件名称,格式为name.jpg等
                'image_mat': image.tolist(), # list格式的图片
            }
            rmq_send(image_info)
    end_time = time.time()
    logger.info(f"sendpics_task down,{cnt} images have been processed,{end_time-start_time} used")

    total_info={
                'uuid': uid, #运行次数标识符,系统一次运行只接受一种uuid
                'count':cnt,
                'total_time':end_time-start_time
            }
    res=requests.post(dispatcher_api.API['imageinfo'],json=total_info)
    logger.info(f"collected down,result is {res.text}")
