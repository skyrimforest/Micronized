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

class StartTimeInfo(BaseModel):
    uuid: str           # id
    count: int          # 第几张
    image_name:str      # 照片名称
    start_time:str            # time needed

class EndTimeInfo(BaseModel):
    uuid: str           # id
    count: int          # 第几张
    image_name:str      # 照片名称

class ResultInfo(BaseModel):
    uuid: str           # 事务id
    weight:float        # 本次运行的权重

class SysConfig(BaseModel):

    pro01memory:float       # pro01的内存
    pro01cpu:float          # pro01的cpu
    pro01reso:float         # 分辨率

    pro02memory:float       # pro02的内存
    pro02cpu:float          # pro02的cpu
    pro02reso: float        # 分辨率
    pro02threshold:float    # pro02的阈值

    pro03memory:float       # pro03的内存
    pro03cpu:float          # pro03的cpu

    bandwidth:int           # 带宽限制