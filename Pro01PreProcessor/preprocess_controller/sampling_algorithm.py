import cv2
import numpy as np
import os
import time
from SkyLogger import get_logger
# sampling algorithm
# input:    video path
# output:   pics and their info

logger = get_logger(__name__)

def frame_fifference(frame01,frame02):
    gray01=cv2.cvtColor(frame01,cv2.COLOR_BGR2GRAY)
    gray02=cv2.cvtColor(frame02,cv2.COLOR_BGR2GRAY)
    diff=cv2.absdiff(gray01,gray02)
    _, thresh = cv2.threshold(diff,30,1,cv2.THRESH_BINARY)
    return thresh

def frame_and(d1,d2):
    result=cv2.bitwise_and(d1,d2)
    return np.sum(result)

# threshold 6000 is assigned by me
def resort_pic(result:int,lower_bound=6000,upper_bound=20000,ratio=1):
    if lower_bound*ratio <= result and result <= upper_bound*ratio:
        return True
    return False

def scale_resort(result:int,new_size:tuple):
    # scale upper and down bound
    ratio=new_size[0]*new_size[1]/(1920*1080)
    return resort_pic(result,ratio=ratio)

def sampling(videoFilePath:str,uid:str)->list:
    logger.info("sampling start")
    file_path = videoFilePath
    video_name=videoFilePath.split('.')[0]
    cap = cv2.VideoCapture(file_path)
    # height weight
    height, width = cap.get(cv2.CAP_PROP_FRAME_HEIGHT),cap.get(cv2.CAP_PROP_FRAME_WIDTH)

    # it is info list
    image_info_li = []
    # 读取视频流帧
    cnt = 0
    count=0
    frame0, frame1, frame2 = None, None, None
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        if ret:
            if cnt == 0:
                frame2 = frame
                cnt += 1
                continue
            elif cnt == 1:
                frame1 = frame2
                frame2 = frame
                cnt += 1
                continue
            frame0 = frame1
            frame1 = frame2
            frame2 = frame
            time_now = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())

            d1 = frame_fifference(frame1, frame0)
            d2 = frame_fifference(frame2, frame1)
            result = frame_and(d1, d2)
            # if resort_pic(result):
            if scale_resort(result,(height,width)):
                count += 1
                # image_info={
                #     'uuid': uid,  # 运行次数标识符,系统一次运行只接受一种uuid
                #     'image_name': video_name+str(cnt)+".jpg",  # 图片文件名称,格式为name.jpg等
                #     'image_mat': frame1,  # list格式的图片
                #     'count':count,
                #     'start_time': time_now
                # }
                image_info={}
                image_info['uuid']=uid
                image_info['image_name']=video_name+str(count)+".jpg"
                image_info['image_mat']=frame1
                image_info['count']=count
                image_info['start_time']=time_now
                image_info_li.append(image_info)
            else:
                continue
    logger.info(f"sampling done")
    return image_info_li
