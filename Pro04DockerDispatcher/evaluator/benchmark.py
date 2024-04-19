
# 该文件返回
# 当reso=1280,threshold=0.7时的最佳结果
# 时延不需要返回,只需要返回一些参数

# d5aef3f4-0957-48d3-95c7-79cfdebe9c4a

from dboperator import query_service
def get_benchmark():
    frame_number = 398
    people = 11.71859296482412
    ratio = 0.2285702662365393
    return [frame_number, people, ratio]


if __name__ == '__main__':
    con,cur=query_service.get_cursor('withlearning')




