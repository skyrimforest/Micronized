from fastapi import APIRouter
from starlette.background import BackgroundTasks
import requests
import time
import numpy as np

from facedetect_controller.FaceDetection import FaceDetection
from schema import PicInfo,ConfigInfo
from API import dispatcher_api,estimator_api

from SkyLogger import get_logger
logger = get_logger("detect")

router = APIRouter(
    prefix="/detect",
    tags=["detect"],
    responses={404: {"description": "Not found"}},
)
def convert_reso(reso):
    if reso==0:
        return 128
    elif reso==1:
        return 160
    elif reso==2:
        return 320
    elif reso==3:
        return 480
    elif reso==4:
        return 640
    elif reso==5:
        return 1280

all_config=ConfigInfo(reso=3,threshold=0.7)
face_detector=None

# 接收图片之后发送图片
# 图片格式为:
# image_info = {
# 'uuid': uid,
# 'image_name': file,
# 'image_mat': image.tolist(),
# }
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
    cnt = 0

def send_analysis(res:dict):
    requests.post(estimator_api.API['recvestimate'],json=res)
    return 0

@router.post("/test")
async def detecttest():
    logger.info("facedetect test success")
    return {"message": "facedetect test success"}

# logic:
#      receive info,
#      give to backen
#      backen send to next phase

@router.post("/recvdetect")
async def recv_detect(picinfo:PicInfo,background_tasks: BackgroundTasks):
    background_tasks.add_task(do_detect,picinfo)
    return {"success": True}


@router.post("/changeconfig")
async def pure_sendpics_controller(ci:ConfigInfo):
    global all_config,face_detector
    all_config=ci
    args = {
        'net_type': 'mb_tiny_RFB_fd',
        'input_size': convert_reso(all_config.reso),
        'threshold': all_config.threshold,
        'candidate_size': 1500,
        'device': 'cuda:0',
    }
    face_detector=FaceDetection(args)
    logger.info(f"config changed to {all_config} success")
    return {
        "message": f"config changed to {all_config} success",
    }
