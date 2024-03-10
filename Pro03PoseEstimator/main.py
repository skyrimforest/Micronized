import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from SkyLogger import get_logger

from poseestimate_controller import controller_estimate

app = FastAPI()
app.include_router(controller_estimate.router)

logger=get_logger('poseestimate')

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

@app.post("/poseestimatetest")
async def poseestimatetest():
    return {"message": "pose estimate success"}

if __name__ == '__main__':
    logger.info('pose estimate start...')
    uvicorn.run("main:app",host="0.0.0.0",port=12002,reload=True)



