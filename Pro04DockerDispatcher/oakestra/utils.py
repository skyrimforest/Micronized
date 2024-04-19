import requests
from API import oakestra_api
import BaseConfig
from SkyLogger import get_logger
import json

logger = get_logger('oakestra')

# 登录,获取token
def login():
    result=requests.post(oakestra_api.API['login'],json={"username":"Admin","password":"Admin"})
    BaseConfig.TOKEN=result.json()['token']
    logger.info("login down")
    header = {"Content-Type": "application/json",
              "Authorization": f"Bearer {BaseConfig.TOKEN}"}
    return header

# 刷新token
def refresh():
    flag=True
    if flag:
        return False
    else:
        login()
        return True

# 注册服务
def application_register(header,descriptor):
    try:
        result=requests.post(oakestra_api.API['appreg'],json=descriptor,headers=header)
        app_list=json.loads(result.json())
        for i in range(0,len(app_list)):
            if app_list[i]['application_name']==descriptor['applications']['application_name']:
                BaseConfig.APPLICATION_ID=app_list[i]['applicationID']
        logger.info(f"{BaseConfig.APPLICATION_ID} register down")
    except:
        logger.info("conflict!!")

# 部署应用中的单个service
def service_deploy(header,service_id):
    result=requests.post(oakestra_api.API['serdeploy']+f'/{service_id}'+'/instance',headers=header)
    print(result)

# 查看应用
def application_show(header,application_id):
    result=requests.get(oakestra_api.API['appreg']+f'/{application_id}',headers=header)
    app_list = json.loads(result.json())
    serviceid_list=app_list['microservices']
    return serviceid_list

# 部署一个应用中的所有service
def application_deploy(header,application_id):
    servicesid_list=application_show(header,application_id)
    for i in servicesid_list:
        service_deploy(header,i)
    logger.info(f"{BaseConfig.APPLICATION_ID} has been deployed")

# 查看簇
def cluster_info(header):
    result=requests.get(oakestra_api.API['clustersinfo'],headers=header)
    logger.info(f"{result.json()} show cluster down")

if __name__ == '__main__':
    header=login()
    # application_show(header,"66224a7a2fcc3d69b8fd77d7")
    application_deploy(header,"66224a7a2fcc3d69b8fd77d7")
    # data = {
    #     "sla_version": "v2.0",
    #     "customerID": "Admin",
    #     "applications": [
    #         {
    #             "applicationID": "",
    #             "application_name": "allin",
    #             "application_namespace": "all",
    #             "application_desc": "An application that contains all containers",
    #             "microservices": [
    #                 {
    #                     "microserviceID": "",
    #                     "microservice_name": "pro01",
    #                     "microservice_namespace": "cvpro",
    #                     "virtualization": "container",
    #                     "memory": 100,
    #                     "vcpus": 1,
    #                     "vgpus": 0,
    #                     "vtpus": 0,
    #                     "bandwidth_in": 0,
    #                     "bandwidth_out": 0,
    #                     "storage": 0,
    #                     "code": "docker.io/library/nginx:latest",
    #                     "state": "",
    #                     "port": "12000:12000"
    #                 },
    #                 {
    #                     "microserviceID": "",
    #                     "microservice_name": "pro02",
    #                     "microservice_namespace": "cvpro",
    #                     "virtualization": "container",
    #                     "memory": 100,
    #                     "vcpus": 1,
    #                     "vgpus": 0,
    #                     "vtpus": 0,
    #                     "bandwidth_in": 0,
    #                     "bandwidth_out": 0,
    #                     "storage": 0,
    #                     "code": "docker.io/library/nginx:latest",
    #                     "state": "",
    #                     "port": "12001:12001"
    #                 },
    #                 {
    #                     "microserviceID": "",
    #                     "microservice_name": "pro03",
    #                     "microservice_namespace": "cvpro",
    #                     "virtualization": "container",
    #                     "memory": 100,
    #                     "vcpus": 1,
    #                     "vgpus": 0,
    #                     "vtpus": 0,
    #                     "bandwidth_in": 0,
    #                     "bandwidth_out": 0,
    #                     "storage": 0,
    #                     "code": "docker.io/library/nginx:latest",
    #                     "state": "",
    #                     "port": "12002:12002"
    #                 },
    #                 {
    #                     "microserviceID": "",
    #                     "microservice_name": "pro04",
    #                     "microservice_namespace": "cvpro",
    #                     "virtualization": "container",
    #                     "memory": 100,
    #                     "vcpus": 1,
    #                     "vgpus": 0,
    #                     "vtpus": 0,
    #                     "bandwidth_in": 0,
    #                     "bandwidth_out": 0,
    #                     "storage": 0,
    #                     "code": "docker.io/library/nginx:latest",
    #                     "state": "",
    #                     "port": "12003:12003"
    #                 }
    #             ]
    #         }
    #     ]
    # }
    # application_register(header,data)
    # service_deploy(header,BaseConfig.APPLICATION_ID)


