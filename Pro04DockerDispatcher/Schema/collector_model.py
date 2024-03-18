from pydantic import BaseModel
class ImageInfo(BaseModel):
    uuid:str            # id
    count:int           # 总共几张
    total_time:float    # 处理总时间

class DetectInfo(BaseModel):
    uuid: str           # id
    count: int          # 第几张
    image_name:str      # 照片名称
    detected:int        # 锚框个数 也就是检测到的人脸数
    total_time: float   # 处理本张的时间

class EstimateInfo(BaseModel):
    uuid: str           # id
    count: int          # 第几张
    image_name:str      # 照片名称
    detected:int        # 人脸数目
    learning:int        # 正在听课
    total_time: float   # 处理本张的时间

class Config(BaseModel):
    uuid: str           # id
    count: int          # 第几张
    image_name:str      # 照片名称
    detected:int        # 人脸数目
    learning:int        # 正在听课
    total_time: float   # 处理本张的时间


