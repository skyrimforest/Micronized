from fastapi import APIRouter
from starlette.background import BackgroundTasks

import BaseConfig
from schema import FilePath,ConfigInfo
from SkyLogger import get_logger
from preprocess_controller.tasks import video_sendpics_task

logger = get_logger("video")

router = APIRouter(
    prefix="/video",
    tags=["video"],
    responses={404: {"description": "Not found"}},
)

all_config=ConfigInfo(threshold=6000,reso=3)

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

@router.post("/test")
async def videotest():
    logger.info("preprocess videotest success")
    return {"message": "preprocess video test success"}

# 纯python发送
@router.post("/sendpics")
async def pure_sendpics_controller(fp:FilePath,background_task:BackgroundTasks):
    global all_config
    logger.info(f"{fp.filePath} starts sending pics")
    reso=convert_reso(all_config.reso)
    vidfilepath=BaseConfig.VID_INPUT_PATH+"/"+fp.filePath+'/'+str(reso)
    threshold=all_config.threshold
    task=fp.task
    background_task.add_task(video_sendpics_task, vidfilepath, threshold, task)
    return {
        "message": f"send {fp.filePath} pics start success",
    }

@router.post("/changeconfig")
async def pure_sendpics_controller(ci:ConfigInfo):
    global all_config
    all_config=ci
    logger.info(f"config changed to {all_config} success")
    return {
        "message": f"config changed to {all_config} success",
    }


if __name__ == '__main__':
    print(all_config.dict())