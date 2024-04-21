import yaml
with open('../dboperator/BestConfigType.yaml', 'r')as yaml_file:
    yaml_obj = yaml.load(yaml_file, Loader=yaml.FullLoader)
    print(yaml_obj)
