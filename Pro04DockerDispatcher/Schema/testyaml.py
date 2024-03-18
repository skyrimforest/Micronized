import yaml
with open('BestConfig.yaml','r')as yaml_file:
    yaml_obj = yaml.load(yaml_file, Loader=yaml.FullLoader)
    print(yaml_obj)
