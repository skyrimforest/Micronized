from fastapi import APIRouter,BackgroundTasks
from fastapi.responses import FileResponse
import BaseConfig
from poseestimate_controller.tasks import recv_draw
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


# 感觉确实是手动触发效果好点..
@router.post("/draw")
async def drawaxis(background_tasks: BackgroundTasks):
    logger.info("draw test")
    background_tasks.add_task(recv_draw)
    return {"message": "poseestimate test success"}

@router.get("/result/{name}")
async def get_pic_result(name: str):
    image_path=BaseConfig.LOG_PATH+'/'+name
    return FileResponse(image_path, media_type="image/jpeg")

# 现在的情况打算做个前端页面,每个阶段手动触发算了
# 手动触发也能获得本次相应的性能指标,
# 通过计算可以自适应调度获取参数,
# 获取参数后通过手动post触发调度.



