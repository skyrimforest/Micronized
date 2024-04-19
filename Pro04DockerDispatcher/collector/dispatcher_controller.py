from fastapi import APIRouter

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

# ----------容器调度相关----------
# 系统开始运行
@router.get("/sysstart")
async def sys_start():
    # 获取初始配置:
    default_config,target=dispatch.get_default_config()

    while True:
        # 注册初始配置:
        new_config=dispatch.get_new_config(default_config,target)

        # 给系统发送现在的配置:
        dispatch.deploy_sys(new_config)

        # 系统实际运行
        dispatch.start_system()

        # 运行结束
        new_target=evaluation.cal_grade()

        default_config=new_config
        target=new_target



