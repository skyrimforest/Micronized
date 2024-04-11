from fastapi import APIRouter
from starlette.background import BackgroundTasks

from facedetect_controller.tasks import do_detect
from schema import *

from SkyLogger import get_logger
logger = get_logger("detect")

router = APIRouter(
    prefix="/detect",
    tags=["detect"],
    responses={404: {"description": "Not found"}},
)

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
