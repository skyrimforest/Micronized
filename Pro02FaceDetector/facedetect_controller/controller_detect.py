from fastapi import APIRouter
from starlette.background import BackgroundTasks

from RMQ import rmq_recv
from facedetect_controller.tasks import my_callback
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


@router.post("/detectstart")
async def detect_start(background_tasks: BackgroundTasks):
    background_tasks.add_task(rmq_recv,my_callback)
