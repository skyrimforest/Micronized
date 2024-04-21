from fastapi import APIRouter
from starlette.background import BackgroundTasks
from Schema.collector_model import config,target
from SkyLogger import get_logger
from evaluator import evaluation
from dispatcher import dispatch

logger = get_logger("dispatcher")

router = APIRouter(
    prefix="/dispatcher",
    tags=["dispatcher"],
    responses={404: {"description": "Not found"}},
)
def optimization_task():
    default_config, target = dispatch.get_default_config()
    new_config = default_config
    new_target = target
    while True:
        # 注册初始配置,并返回新配置
        new_config = dispatch.get_new_config(new_config, new_target)

        # 给系统发送现在的配置:
        dispatch.deploy_sys(new_config)

        # 运行结束,获取运行结果
        new_target = dispatch.black_box_function()

        logger.info(f"new config:{new_config},new target:{new_target}")

# ----------容器调度相关----------
# 系统开始运行
@router.get("/sysstart")
async def sys_start(background_tasks: BackgroundTasks):
    background_tasks.add_task(optimization_task)



