import BaseConfig
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from SkyLogger import get_logger

from poseestimate_controller import controller_estimate,tasks_outofdate
from poseestimate_controller.FaceAlignment import FaceAlignmentCNN

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

# @app.on_event('startup')
# def init_data():
#     args = {
#         'lite_version': False,
#         'model': 'hopenet',
#         'batch_size': 1,
#         'device': 'cuda:0',
#     }
#     tasks.face_alignment =  FaceAlignmentCNN(args)

@app.post("/poseestimatetest")
async def poseestimatetest():
    return {"message": "pose estimate success"}

if __name__ == '__main__':
    logger.info('pose estimate start...')
    uvicorn.run("main:app",host="0.0.0.0",port=int(BaseConfig.ESTIMATOR_PORT),reload=True)



