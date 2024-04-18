from optimizer.optimization import my_optimizer,my_utility


# 获取BestConfig.yaml
def get_default_config():
    pass


# 给系统注册配置项,并返回新配置项
def get_new_config(new_config,new_target):
    new_config = new_config.model_dump()
    new_target = new_target.model_dump()
    my_optimizer.register(params=new_config, target=new_target['target'])
    next_point = my_optimizer.suggest(my_utility)
    return next_point


def deploy_sys():
    pass


def start_system():
    pass