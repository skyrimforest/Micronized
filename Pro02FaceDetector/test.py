import requests
import BaseConfig
from API import dispatcher_api
if __name__ == '__main__':
    data={
        "uuid":"test",
        "image_name": "sky",
        "boxes": 3,
        "count":5,
        "total_time":2.33
    }
    print(data)
    res=requests.post(dispatcher_api.API['detectinfo'],json=data)
    print(res.text)