import BaseConfig

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from SkyLogger import get_logger
from collector import collector_controller
# from preprocess_controller import controller_pics

app = FastAPI()
app.include_router(collector_controller.router)

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

if __name__ == '__main__':
    logger.info('dispatcher start...')
    uvicorn.run("main:app",host="0.0.0.0",port=int(BaseConfig.DISPATCHER_PORT),reload=True)



