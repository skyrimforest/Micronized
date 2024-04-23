from pydantic import BaseModel

class FilePath(BaseModel):
    filePath: str

class PicInfo(BaseModel):
    uuid: str
    count:int
    image_name:str
    image_mat:list

class DetectRes(BaseModel):
    uuid:str
    count:int
    image_name:str
    image_mat:list
    boxes:list

class ConfigInfo(BaseModel):
    reso:int
    threshold:float

