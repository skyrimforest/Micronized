import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from SkyLogger import get_logger
import BaseConfig
from facedetect_controller import controller_detect,tasks
from facedetect_controller.FaceDetection import FaceDetection

app = FastAPI()
app.include_router(controller_detect.router)

logger=get_logger('facedetect')

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


@app.on_event('startup')
def init_data():
    args = {
        'net_type': 'mb_tiny_RFB_fd',
        'input_size': 480,
        'threshold': 0.7,
        'candidate_size': 1500,
        'device': 'cuda:0',
    }
    tasks.face_detector = FaceDetection(args)

@app.post("/facedetecttest")
async def facedetecttest():
    return {"message": "facedetect test success"}

if __name__ == '__main__':
    logger.info('facedetect start...')
    uvicorn.run("main:app",host="0.0.0.0",port=int(BaseConfig.DETECTOR_PORT),reload=True)



