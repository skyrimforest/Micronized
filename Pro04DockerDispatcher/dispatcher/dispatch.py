import requests
import yaml

from optimizer.optimization import my_optimizer,my_utility
from dboperator import query_service
from evaluator import evaluation
from API import preprocess_api,detection_api,estimation_api
from SkyLogger import get_logger

logger = get_logger('dispatcher')

def get_best_config():
    # 获取最优配置
    with open('../config/BestConfig.yaml', 'r', encoding='utf-8') as yaml_file:
        yaml_obj = yaml.load(yaml_file, Loader=yaml.FullLoader)
    config = yaml_obj['bestconfig']['transaction']

    # 获取最优配置的目标值
    con, cur = query_service.get_cursor('database')
    target_uuid = yaml_obj["bestconfig"]["uuid"]
    get_target_sql = f"select * from configinfo where uuid='{target_uuid}'"
    result = query_service.select_ope(cur, get_target_sql)
    if len(result) != 0:
        target = result[0][2]
    else:
        target = 233

    global steps
    steps= yaml_obj['bestconfig']['generation']
    return config, float(target)


# 写每次迭代的结果
def write_each_iterator(uuid, config):
    # 写config
    # 获取最优配置
    global steps
    for item in config:
        config[item]=float(config[item])
    data = {
        'bestconfig': {
            'uuid': uuid,
            'generation':steps,
            'transaction': config
        }
    }
    with open(f'./config/CurrentConfig{steps}.yaml', 'w', encoding='utf-8') as yaml_file:
        yaml.dump(data, yaml_file)

# 获取写最优配置
def write_best_config(uuid,config, target):
    # 写config
    # 获取最优配置
    global steps
    for item in config:
        config[item] = float(config[item])
    data = {
        'bestconfig': {
            'uuid': uuid,
            'generation': steps,
            'transaction': config
        }
    }
    with open(f'./config/BestConfigType.yaml', 'w', encoding='utf-8') as yaml_file:
        yaml.dump(data, yaml_file)
    # 写target
    con, cur = query_service.get_cursor('database')
    data = (uuid, target,)
    insert_config_sql = """
              insert into configinfo (uuid,weight)
             VALUES (?,?)
             """
    query_service.insert_ope(cur, insert_config_sql, data)
    query_service.delete_cursor(con, cur)


# 给系统注册配置项,并返回新配置项
def get_new_config(new_config:dict,new_target:float):
    new_config = new_config
    new_target = new_target
    my_optimizer.register(params=new_config, target=new_target)
    next_point = my_optimizer.suggest(my_utility)
    return next_point

# 部署预处理
def deploy_preprocess(config):
    # 修改模块参数
    true_config={
        'threshold':config['pro01threshold'],
        'reso':config['pro01reso'],
    }
    requests.post(preprocess_api.API['changeconfig'],json=true_config)
    logger.info('preprocess deploy success')
    # 修改oakestra参数

# 部署面部检测
def deploy_detection(config):
    # 修改模块参数
    true_config = {
        'threshold': config['pro02threshold'],
        'reso': config['pro02reso'],
    }
    requests.post(detection_api.API['changeconfig'], json=true_config)
    logger.info('preprocess deploy success')
    # 修改oakestra参数


# 部署姿态估计
def deploy_estimation(config):
    # 修改模块参数
    # 实际上并没有
    # 修改oakestra参数
    # todo
    pass

def deploy_network(config):
    pass



def start_system():
    requests.post()
    logger.info("System dispatch start")

# 转换字典的参数
def int_para(next_point):
    for item in next_point:
        next_point[item] = int(next_point[item])
    return next_point
def deploy_sys(next_point):
    # 部署预处理阶段配置
    deploy_preprocess()
    # 部署面部检测阶段配置
    deploy_detection()
    # 部署姿态估计阶段配置
    deploy_estimation()
    # 部署网络配置
    deploy_network()
    # 启动系统
    start_system()


# 黑盒函数,获取分数后存到db中
def black_box_function():
    # 获取事务uid
    uid=evaluation.get_latest_uid()
    # 获取事务分数
    grade=evaluation.cal_grade(uid)
    return grade

# # 待优化函数,用于处理整型与浮点
# def function_2b_optimized(next_point):
#     # 整数化所有参数
#     next_point=int_para(next_point)
#     # 部署该配置
#     deploy_sys(next_point)
#     # 获取指令后进行下一步
#     # 返回得分
#     grade=black_box_function()
#     return grade
#
# def get_target():
#


if __name__ == '__main__':

    # 系统初始化
    config,target=get_best_config()
    print(config)
    for i in range(0,10):
        new_config=get_new_config(config,target)
    # # 部署系统
    # int_para(new_config)
    # deploy_sys(new_config)
    #
    # # 获取权值
    # new_target=black_box_function()
    #
    # # 系统再部署
    # get_new_config(new_config,new_target)

        deploy_detection(new_config)