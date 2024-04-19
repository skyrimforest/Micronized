import numpy as np

from dboperator import query_service
import benchmark
database_name='withlearning'
# 获取预处理阶段的信息
# 该次事务预处理阶段的总照片数与总时延
def eva_preprocess(uuid):
    con, cur = query_service.get_cursor(database_name)
    sql_query = f"SELECT * FROM imageinfo WHERE uuid='{uuid}'"
    res=query_service.select_ope(cur,sql_query)
    query_service.delete_cursor(con,cur)
    frame_number=float(res[0][2])
    time=float(res[0][3])
    # 照片数量+平均时延
    return frame_number,time/frame_number

# 获取面部检测阶段的信息
# 每张图的平均识别人数与平均时延
def eva_detection(uuid):
    try:
        con, cur = query_service.get_cursor(database_name)
        sql_query = f"SELECT * FROM detectinfo WHERE uuid='{uuid}'"
        res=query_service.select_ope(cur,sql_query)
        query_service.delete_cursor(con,cur)
        people_number=0.0
        time=0.0
        number=len(res)
        for i in res:
            people_number+=float(i[4])
            time+=float(i[5])
        # 人的平均数量+平均时延
        ave_people=people_number/number
        ave_time=time/number
        return ave_people,ave_time
    except:
        return 0,10

# 获取姿态估计阶段的信息
def eva_estimation(uuid):
    try:
        con, cur = query_service.get_cursor(database_name)
        sql_query = f"SELECT * FROM estimateinfo WHERE uuid='{uuid}'"
        res = query_service.select_ope(cur, sql_query)
        query_service.delete_cursor(con, cur)
        learning_ratio=0.0
        time = 0.0
        number = len(res)
        for i in res:
            # 学习人数比检测人数
            learning_ratio+=float(i[5])/float(i[4])
            time += float(i[6])
        # 平均学习率+平均时延
        ave_ratio = learning_ratio / number
        ave_time =time / number
        return ave_ratio,ave_time
    except:
        return 0,10

# 计算总得分
def cal_grade(uuid):
    frame_number,time_pre=eva_preprocess(uuid)
    people_number,time_det=eva_detection(uuid)
    learning_ratio,time_est=eva_estimation(uuid)
    bench_mark=benchmark.get_benchmark()
    indexes=np.array([frame_number/bench_mark[0],people_number/bench_mark[1],learning_ratio/bench_mark[2],time_pre,time_det,time_est])

    print(indexes)
    weight=np.array([
        1,1,1,
        -1,-1,-1
    ])

    print(weight)
    grade=np.dot(indexes,weight)
    return grade



if __name__ == '__main__':
    grade=cal_grade('80d86399-63bd-4367-83ab-caefdbf33099')
    print(grade)