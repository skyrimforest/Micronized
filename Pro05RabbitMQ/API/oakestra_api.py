import BaseConfig

PREFIX='http://' + BaseConfig.OAKESTRA_IP + ':' + BaseConfig.OAKESTRA_PORT+'/api/'

API={
    'login':'auth/login',
    'appreg':'application',
    'serdeploy':'service',
    'clustersinfo':'clusters/active'
}

for item in API:
    API[item]=PREFIX+API[item]