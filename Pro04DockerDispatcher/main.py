import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import BaseConfig
from SkyLogger import get_logger
from collector import collector_controller,dispatcher_controller


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


if __name__ == '__main__':
    logger.info('dispatcher start...')
    uvicorn.run("main:app",host="0.0.0.0",port=int(BaseConfig.DISPATCHER_PORT),reload=True)



