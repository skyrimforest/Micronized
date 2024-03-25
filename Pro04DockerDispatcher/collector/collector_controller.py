from fastapi import APIRouter
from Schema import collector_model
from SkyLogger import get_logger
from dboperator import query_service
logger = get_logger("collector")

router = APIRouter(
    prefix="/collector",
    tags=["collector"],
    responses={404: {"description": "Not found"}},
)

@router.post("/test")
async def picstest():
    logger.info("dispatcher collector test success")
    return {"message": "dispatcher collector test success"}

# start time collect
@router.post("/starttime")
async def get_starttime(time_info:collector_model.StartTimeInfo):
    insert_starttime_sql = """
         insert into startinfo (uuid, count, image_name,start_time)
        VALUES (?, ?, ?,?)
        """
    data = (time_info.uuid, time_info.count, time_info.image_name,time_info.start_time)
    query_service.do_insert(insert_starttime_sql, data)
    return {"success": True}

# end time collect
@router.post("/endtime")
async def get_endtime(time_info:collector_model.EndTimeInfo):
    insert_endtime_sql = """
         insert into endinfo (uuid, count, image_name)
        VALUES (?, ?, ?)
        """
    data = (time_info.uuid, time_info.count, time_info.image_name)
    query_service.do_insert(insert_endtime_sql, data)
    return {"success": True}

# 预处理模块信息收集
@router.post("/imageinfo")
async def imageinfo_collector(image_info:collector_model.ImageInfo):
    insert_imageinfo_sql="""
     insert into imageinfo (uuid, count, total_time)
    VALUES (?, ?, ?)
    """
    data=(image_info.uuid,image_info.count,image_info.total_time)
    query_service.do_insert(insert_imageinfo_sql,data)
    return {"success":True}

@router.get("/imageinfo")
async def imageinfo_collector():
    select_imageinfo_sql="""
     select * from imageinfo
    """
    result=query_service.do_select(select_imageinfo_sql)
    res_dict=[]
    for row in result:
        temp={
            "id":row[0],
            "uuid":row[1],
            "count":row[2],
            "total_time":row[3],
            "start_time":row[4],
        }
        res_dict.append(temp)
    return {"success":True,"data":res_dict}

# 面部识别信息收集
@router.post("/detectinfo")
async def detectinfo_collector(detect_info:collector_model.DetectInfo):
    insert_detectinfo_sql = """
        insert into detectinfo (uuid,count,image_name,detected, total_time)
       VALUES (?, ?, ?, ?,?)
       """
    data = (detect_info.uuid, detect_info.count,detect_info.image_name, detect_info.detected,detect_info.total_time)
    query_service.do_insert(insert_detectinfo_sql, data)
    return {"success": True}

@router.get("/detectinfo")
async def detectinfo_collector():
    select_detectinfo_sql = """
       select * from detectinfo
      """
    result = query_service.do_select(select_detectinfo_sql)
    res_dict = []
    for row in result:
        temp = {
            "id": row[0],
            "uuid": row[1],
            "count": row[2],
            "image_name": row[3],
            "detected": row[4],
            "total_time": row[5],
            "start_time": row[6],
        }
        res_dict.append(temp)
    return {"success": True, "data": res_dict}


# 姿态检测信息识别
@router.post("/estimateinfo")
async def estimateinfo_collector(estimate_info:collector_model.EstimateInfo):
    insert_estimateinfo_sql = """
           insert into estimateinfo (uuid,count,image_name,detected,learning, total_time)
          VALUES (?, ?, ?, ?, ?,?)
          """
    data = (estimate_info.uuid, estimate_info.count,estimate_info.image_name, estimate_info.detected,estimate_info.learning, estimate_info.total_time)
    query_service.do_insert(insert_estimateinfo_sql, data)
    return {"success": True}

@router.get("/estimateinfo")
async def estimateinfo_collector():
    select_estimateinfo_sql = """
          select * from estimateinfo
         """
    result = query_service.do_select(select_estimateinfo_sql)
    res_dict = []
    for row in result:
        temp = {
            "id": row[0],
            "uuid": row[1],
            "count": row[2],
            "image_name": row[3],
            "detected": row[4],
            "learning":row[5],
            "total_time": row[6],
            "start_time": row[7],
        }
        res_dict.append(temp)
    return {"success": True, "data": res_dict}


# 容器调度相关


