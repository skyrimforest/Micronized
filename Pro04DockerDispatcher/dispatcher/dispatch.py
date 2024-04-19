from optimizer.optimization import my_optimizer,my_utility
from dboperator import query_service

import yaml

# 获取BestConfig.yaml
def get_default_config():
    # 获取最优配置
    with open('../dboperator/BestConfig.yaml', 'r',encoding='utf-8') as yaml_file:
        yaml_obj = yaml.load(yaml_file, Loader=yaml.FullLoader)

    # 获取最优配置的目标值
    con,cur=query_service.get_cursor('database')
    target_uuid=yaml_obj["bestconfig"]["uuid"]
    get_target_sql=f"select * from configinfo where uuid='{target_uuid}'"
    result=query_service.select_ope(cur,get_target_sql)
    if len(result)!=0:
        target=result[2]
    else:
        target=233
    query_service.delete_cursor(con,cur)
    return yaml_obj,float(target)

# 给系统注册配置项,并返回新配置项
def get_new_config(new_config:dict,new_target:float):
    new_config = new_config['transaction']
    new_target = new_target
    my_optimizer.register(params=new_config, target=new_target)
    next_point = my_optimizer.suggest(my_utility)
    return next_point

def deploy_sys():
    pass

def start_system():
    pass


if __name__ == '__main__':
    config,target=get_default_config()
    print(config)
    print(target)
    new_config=get_new_config(config['bestconfig'],target)