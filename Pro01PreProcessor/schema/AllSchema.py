from pydantic import BaseModel

class FilePath(BaseModel):
    filePath: str
    task:str

class PicInfo(BaseModel):
    uuid: str
    count:int
    image_name:str
    image_mat:list

class ConfigInfo(BaseModel):
    threshold:int
    reso:int