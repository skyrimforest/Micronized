import BaseConfig

PREFIX='http://' + BaseConfig.DISPATCHER_IP + ':' + BaseConfig.DISPATCHER_PORT
# PREFIX='http://' + 'localhost' + ':' + BaseConfig.DISPATCHER_PORT

API={
    'detectinfo': '/collector/detectinfo'
}

for item in API:
    API[item]=PREFIX+API[item]