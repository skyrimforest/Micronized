from fastapi import APIRouter
from starlette.background import BackgroundTasks

import BaseConfig
from schema import FilePath
from SkyLogger import get_logger
from preprocess_controller.tasks import video_sendpics_task

logger = get_logger("video")

router = APIRouter(
    prefix="/video",
    tags=["video"],
    responses={404: {"description": "Not found"}},
)

@router.post("/test")
async def videotest():
    logger.info("preprocess videotest success")
    return {"message": "preprocess video test success"}

# 纯python发送
@router.post("/sendpics")
async def pure_sendpics_controller(fp:FilePath,background_task:BackgroundTasks):
    logger.info(f"{fp.filePath} starts sending pics")
    vidfilepath=BaseConfig.VID_INPUT_PATH+"/"+fp.filePath
    background_task.add_task(video_sendpics_task,vidfilepath)
    return {
        "message": f"send {fp.filePath} pics start success",
    }

