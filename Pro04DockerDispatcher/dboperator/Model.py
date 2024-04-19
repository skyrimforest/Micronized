import sqlite3
from datetime import datetime

conn=sqlite3.connect("database.db")
cur=conn.cursor()

# 表1: imageinfo
# 表2: detectinfo
# 表3: estimateinfo

# ------------创建阶段------------

# class ImageInfo(BaseModel):
#     uuid:str            # id
#     count:int           # 总共几张
#     total_time:float    # 处理总时间
image_info_table_sql="""
create table if not exists imageinfo (
    id INTEGER PRIMARY KEY,
    uuid TEXT,
    count INTEGER,
    total_time FLOAT,
    start_time TEXT DEFAULT (strftime('%Y-%m-%d %H:%M:%S','now','localtime'))
)
"""
# class DetectInfo(BaseModel):
#     uuid: str           # id
#     count: int          # 第几张
#     image_name:str      # 照片名称
#     detected:int        # 锚框个数 也就是检测到的人脸数
#     total_time: float   # 处理本张的时间
detect_info_table_sql="""
create table if not exists detectinfo(
    id INTEGER PRIMARY KEY,
    uuid TEXT,
    count INTEGER,
    image_name TEXT,
    detected INTEGER,
    total_time FLOAT,
    start_time TEXT DEFAULT (strftime('%Y-%m-%d %H:%M:%S','now', 'localtime'))
)

"""
# class EstimateInfo(BaseModel):
#     uuid: str           # id
#     count: int          # 第几张
#     image_name:str      # 照片名称
#     detected:int        # 人脸数目
#     learning:int        # 正在听课
#     total_time: float   # 处理本张的时间
estimate_info_table_sql="""
create table if not exists estimateinfo(
    id INTEGER PRIMARY KEY,
    uuid TEXT,
    count INTEGER,
    image_name TEXT,
    detected INTEGER,
    learning INTEGER,
    total_time FLOAT,
    start_time TEXT DEFAULT (strftime('%Y-%m-%d %H:%M:%S','now', 'localtime'))
)
"""

# result info包括:
result_info_table_sql="""
create table if not exists resultinfo(
    id INTEGER PRIMARY KEY,
    uuid TEXT,
    count INTEGER,
    image_name TEXT,
    detected INTEGER,
    learning INTEGER,
    total_time FLOAT,
    start_time TEXT DEFAULT (strftime('%Y-%m-%d %H:%M:%S','now', 'localtime'))
)

"""
# to record real start time we should count from info haven't been created.
# class StartTimeInfo(BaseModel):
#     uuid: str           # id
#     count: int          # 第几张
#     image_name:str      # 照片名称
#     time:str            # time needed
start_info_table_sql="""
create table if not exists startinfo(
    id INTEGER PRIMARY KEY,
    uuid TEXT,
    count INTEGER,
    image_name TEXT,
    start_time TEXT
)

"""
# class EndTimeInfo(BaseModel):
#     uuid: str           # id
#     count: int          # 第几张
#     image_name:str      # 照片名称
end_info_table_sql="""
create table if not exists endinfo(
    id INTEGER PRIMARY KEY,
    uuid TEXT,
    count INTEGER,
    image_name TEXT,
    end_time TEXT DEFAULT (strftime('%Y-%m-%d %H:%M:%S','now', 'localtime'))
)
"""

# class ConfigInfo(BaseModel):
#     uuid: str           # id
#     weight:FLOAT      # 照片名称
config_info_table_sql="""
create table if not exists configinfo(
    id INTEGER PRIMARY KEY,
    uuid TEXT,
    weight FLOAT,
    end_time TEXT DEFAULT (strftime('%Y-%m-%d %H:%M:%S','now', 'localtime'))
)
"""


cur.execute(
    image_info_table_sql
)

cur.execute(
    detect_info_table_sql
)

cur.execute(
    estimate_info_table_sql
)

cur.execute(
    start_info_table_sql
)

cur.execute(
    end_info_table_sql
)

cur.execute(
    config_info_table_sql
)

# current_time = datetime.now()
# formatted_time = current_time.strftime('%Y-%m-%d %H:%M:%S')
# test_insert_sql=
# insert into imageinfo (uuid, count, total_time)
# VALUES (?, ?, ?)
# """
# cur.execute(
#     test_insert_sql,("testid",23,1.72)
# )

conn.commit()
conn.close()

