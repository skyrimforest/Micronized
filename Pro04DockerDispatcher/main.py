import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import BaseConfig
from SkyLogger import get_logger
from collector import collector_controller,dispatcher_controller
from optimizer import optimization
from optimizer.bayesian_optimizor import BayesianOptimization,UtilityFunction
from optimizer.experience_buffer import ExpBuffer
# from preprocess_controller import controller_pics
import requests
import API


app = FastAPI()
app.include_router(collector_controller.router)
app.include_router(dispatcher_controller.router)

logger=get_logger('dispatcher')

origins = [
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/dispatchtest")
async def dispatchtest():
    return {"message": "dispatch test success"}

@app.on_event('startup')
def init_data():

    #----------配置初始化----------
    BaseConfig.APPLICATION_ID = '233333'

    #----------优化器初始化----------
    optimization.my_buffer=ExpBuffer()
    optimization.my_optimizer=BayesianOptimization(
    f=None,
    pbounds={'x': (-2, 6), 'y': (-3, 8)},
    verbose=2,
    random_state=1,
    exp_buffer=optimization.my_buffer,
    allow_duplicate_points=True
    )
    optimization.my_utility=UtilityFunction(kind="ucb", kappa=2.5, xi=0.0)


if __name__ == '__main__':
    logger.info('dispatcher start...')
    uvicorn.run("main:app",host="0.0.0.0",port=int(BaseConfig.DISPATCHER_PORT),reload=True)



