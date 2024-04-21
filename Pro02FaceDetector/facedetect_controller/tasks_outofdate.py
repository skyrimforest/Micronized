import time
import numpy as np
import requests

from schema import *
from API import dispatcher_api,estimator_api

from SkyLogger import get_logger
logger = get_logger("tasks")

# args = {
#     'net_type': 'mb_tiny_RFB_fd',
#     'input_size': 480,
#     'threshold': 0.7,
#     'candidate_size': 1500,
#     'device': 'cuda:0',
# }
# face_detection = FaceDetection(args)
# 接收图片之后发送图片
# 图片格式为:
# image_info = {
# 'uuid': uid,
# 'image_name': file,
# 'image_mat': image.tolist(),
# }
# cnt用于记录图片数量
cnt=0
def do_detect(picinfo:PicInfo):
    start = time.time()
    body=picinfo.dict()
    # packet is wrong then drop it
    try:
        image = np.array(body['image_mat'], dtype=np.uint8)
        image_name = body['image_name']
        logger.info(f"{image_name} start to detect ")
        boxes, labels, probs = face_detector(image)
        image_info = {
            'uuid': body['uuid'],
            'image_name': image_name,
            'image_mat': image.tolist(),
            'boxes': boxes.tolist(),
        }
        # 发送给下一阶段流水线
        send_analysis(image_info)
    except:
        return {
            "success": False
        }

    global cnt
    cnt+=1
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

def send_analysis(res:dict):
    requests.post(estimator_api.API['recvestimate'],json=res)
    return 0