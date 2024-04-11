from fastapi import APIRouter,BackgroundTasks
from fastapi.responses import FileResponse
import BaseConfig
from poseestimate_controller.tasks import recv_draw
from schema import *
from SkyLogger import get_logger
logger = get_logger("estimate")

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

