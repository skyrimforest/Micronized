from fastapi import APIRouter
from starlette.background import BackgroundTasks

import BaseConfig
from schema import FilePath
from SkyLogger import get_logger
from preprocess_controller.tasks import pics_sendpics_task

logger = get_logger("pics")

router = APIRouter(
    prefix="/pics",
    tags=["pics"],
    responses={404: {"description": "Not found"}},
)

@router.post("/test")
async def picstest():
    logger.info("preprocess pics test success")
    return {"message": "preprocess pics test success"}

# 纯python发送
@router.post("/sendpics")
async def pure_sendpics_controller(fp:FilePath,background_task:BackgroundTasks):
    logger.info(f"{fp.filePath} starts sending pics")
    picfilepath=BaseConfig.PIC_INPUT_PATH+"/"+fp.filePath
    background_task.add_task(pics_sendpics_task,picfilepath)
    return {
        "message": f"send {fp.filePath} pics start success",
    }

