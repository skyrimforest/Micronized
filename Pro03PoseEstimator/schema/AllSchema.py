from pydantic import BaseModel

class FilePath(BaseModel):
    filePath: str

class PicInfo(BaseModel):
    uuid: str
    image_name:str
    image_mat:list

class DetectRes(BaseModel):
    uuid:str
    image_name:str
    image_mat:list
    boxes:list


