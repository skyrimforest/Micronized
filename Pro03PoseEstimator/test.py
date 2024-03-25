import requests
import time
import BaseConfig
from API import dispatcher_api
if __name__ == '__main__':

    end_time_info={
        'uuid': '23333',  # 运行次数标识符,系统一次运行只接受一种uuid
        'count': 233,
        'image_name': "test.png"
    }
    # push end time to db
    res=requests.post(dispatcher_api.API['endtime'],json=end_time_info)
    print(res.text)
# import requests
# import BaseConfig
# from API import dispatcher_api
#
# if __name__ == '__main__':
#     filePath={
#         'filePath':'/handshaking'
#     }
#     res = requests.post("http://localhost:12000/pics/sendpics", json=filePath)

