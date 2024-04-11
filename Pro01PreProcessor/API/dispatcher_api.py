import BaseConfig

PREFIX='http://' + BaseConfig.DISPATCHER_IP + ':' + BaseConfig.DISPATCHER_PORT

API={
    'imageinfo':'/collector/imageinfo',
    'starttime':'/collector/starttime'
}

for item in API:
    API[item]=PREFIX+API[item]