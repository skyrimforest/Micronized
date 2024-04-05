import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import BaseConfig
from SkyLogger import get_logger

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

@app.post("/test")
async def preprocesstest():
    return {"message": "preprocess test success"}

if __name__ == '__main__':
    logger.info('preprocessor start...')
    uvicorn.run("main:app",host="0.0.0.0",port=BaseConfig.OWN_PORT,reload=True)



