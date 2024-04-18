import BaseConfig

PREFIX='http://' + BaseConfig.OAKESTRA_IP + ':' + BaseConfig.OAKESTRA_PORT+'/api/'

API={
    'login':'auth/login',
    'starttime':'/collector/starttime'
}

for item in API:
    API[item]=PREFIX+API[item]