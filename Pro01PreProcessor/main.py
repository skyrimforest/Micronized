import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from SkyLogger import get_logger

from preprocess_controller import controller_pics

app = FastAPI()
app.include_router(controller_pics.router)

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
    uvicorn.run("main:app",host="0.0.0.0",port=12000,reload=True)



