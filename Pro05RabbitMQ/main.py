import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from service import net_service

from Schema.AllSchema import ConfigInfo
import BaseConfig

from SkyLogger import get_logger


app = FastAPI()

origins = [
    "*",
]

logger=get_logger('net')

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

all_config=ConfigInfo(bandwidth=2000)

@app.post("/dispatchtest")
async def dispatchtest():
    return {"message": "dispatch test success"}

@app.on_event('startup')
def init_data():
    global all_config
    net_service.set_bandwidth_limit(all_config.bandwidth)

@app.post("/changeconfig")
async def pure_sendpics_controller(ci:ConfigInfo):
    global all_config
    all_config=ci
    net_service.set_bandwidth_limit(all_config.bandwidth)
    return {
        "message": f"config changed to {all_config} success",
    }


if __name__ == '__main__':
    uvicorn.run("main:app",host="0.0.0.0",port=int(BaseConfig.NET_PORT),reload=True)



