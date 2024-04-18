import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import BaseConfig
from SkyLogger import get_logger
from schema import *


from preprocess_controller import controller_pics,controller_video
app = FastAPI()
app.include_router(controller_pics.router)
app.include_router(controller_video.router)

logger=get_logger('preprocessor')

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

@app.post("/testpicinfo")
async def preprocesstest(picinfo:PicInfo):
    print(picinfo.dict())
    return {"message": "preprocess test success"}

if __name__ == '__main__':
    logger.info('preprocessor start...')
    uvicorn.run("main:app",host="0.0.0.0",port=int(BaseConfig.PREPROCESSOR_PORT),reload=True)



