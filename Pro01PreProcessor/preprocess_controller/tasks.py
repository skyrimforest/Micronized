# this will be used to record edge2edge time cost
#
import requests

import BaseConfig
from RMQ import rmq_send
import os
import time
import cv2
from SkyLogger import get_logger
import uuid
from API import dispatcher_api
from .sampling_algorithm import sampling

logger = get_logger("tasks")

def pics_sendpics_task(picsFilePath:str):
    logger.info("pics sendpics_task start")

    start_time = time.time()
    cnt=0
    uid=str(uuid.uuid4())
    for root, dirs, files in os.walk(picsFilePath):
        for file in files:
            # record start time
            time_now = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())


            file_path = picsFilePath + '/' + file
            image = cv2.imread(file_path)
            image_info = {
                'uuid': uid, #运行次数标识符,系统一次运行只接受一种uuid
                'image_name': file, # 图片文件名称,格式为name.jpg等
                'image_mat': image.tolist(), # list格式的图片
            }
            cnt += 1
            rmq_send(image_info)

            # send each pic's start time info to db
            start_time_info = {
                'uuid': uid,  # 运行次数标识符,系统一次运行只接受一种uuid
                'count': cnt,
                'image_name': image_info['image_name'],
                'start_time':time_now
            }
            requests.post(dispatcher_api.API['starttime'], json=start_time_info)

    end_time = time.time()
    logger.info(f"pics_sendpics_task down,{cnt} images have been processed,{end_time-start_time} used")

    total_info={
                'uuid': uid, #运行次数标识符,系统一次运行只接受一种uuid
                'count':cnt,
                'total_time':end_time-start_time
            }

    # send log info to db
    res=requests.post(dispatcher_api.API['imageinfo'],json=total_info)
    logger.info(f"collected down,result is {res.text}")

def video_sendpics_task(videoFilePath:str):
    logger.info("video sendpics_task start")
    start_time = time.time()
    cnt=0
    uid=str(uuid.uuid4())
    for root, dirs, files in os.walk(videoFilePath):
        for file in files:
            file_path = videoFilePath + '/' + file
            logger.info(f"{file_path} start")

            image_info_li=sampling(file_path,uid)

            for image_info in image_info_li:
                real_image_info = {
                    'uuid': image_info['uuid'], #运行次数标识符,系统一次运行只接受一种uuid
                    'image_name': image_info['image_name'], # 图片文件名称,格式为name.jpg等
                    'image_mat': image_info['image_mat'].tolist(), # list格式的图片
                }
                cnt += 1
                rmq_send(real_image_info)
                # send each pic's start time info to db
                start_time_info = {
                    'uuid': image_info['uuid'],  # 运行次数标识符,系统一次运行只接受一种uuid
                    'count': image_info['count'],
                    'image_name': image_info['image_name'],
                    'start_time': image_info['start_time']
                }
                requests.post(dispatcher_api.API['starttime'], json=start_time_info)

    end_time = time.time()
    logger.info(f"video_sendpics_task down,{cnt} images have been processed,{end_time-start_time} used")

    total_info={
                'uuid': uid, #运行次数标识符,系统一次运行只接受一种uuid
                'count':cnt,
                'total_time':end_time-start_time
            }
    res=requests.post(dispatcher_api.API['imageinfo'],json=total_info)
    logger.info(f"collected down,result is {res.text}")

