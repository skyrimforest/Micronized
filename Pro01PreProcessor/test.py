import requests
import time
import BaseConfig
from API import dispatcher_api
if __name__ == '__main__':

    time_now = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())

    # send time info to db
    start_time_info = {
        'uuid': 'testuuid',  # 运行次数标识符,系统一次运行只接受一种uuid
        'count': 2333,
        'image_name': 'test.png',
        'start_time': time_now
    }
    res=requests.post(dispatcher_api.API['starttime'], json=start_time_info)
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

