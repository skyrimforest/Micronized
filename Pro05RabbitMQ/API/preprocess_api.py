import BaseConfig

PREFIX='http://' + BaseConfig.PREPROCESSOR_IP + ':' + BaseConfig.PREPROCESSOR_PORT+'/'

API={
    'login':'auth/login',
    'appreg':'application',
    'serdeploy':'service',
    'clustersinfo':'clusters/active'
}

for item in API:
    API[item]=PREFIX+API[item]