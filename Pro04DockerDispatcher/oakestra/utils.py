import requests
import API
import BaseConfig

# 登录,获取token
def login():
    result=requests.post(API.oakestra_api['login'],json={"username":"Admin","password":"Admin"})
    BaseConfig.TOKEN=result.json()['token']

# 刷新token
def refresh():
    if True:
        pass
    else:
        login()


# 发送消息
def sendinfo():
    pass


