# import requests
# import BaseConfig
# from API import dispatcher_api
# if __name__ == '__main__':
#
#     total_info={
#                 'uuid': "test", #运行次数标识符,系统一次运行只接受一种uuid
#                 'count':3,
#                 'total_time':2.33
#             }
#     print(type(total_info['uuid']))
#     print(type(total_info['count']))
#     print(type(total_info['total_time']))
#     res=requests.post(dispatcher_api.API['imageinfo'],json=total_info)
#     print(res.text)
import requests
import BaseConfig
from API import dispatcher_api

if __name__ == '__main__':
    filePath={
        'filePath':'/handshaking'
    }
    res = requests.post("http://localhost:12000/pics/sendpics", json=filePath)

