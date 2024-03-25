import BaseConfig

PREFIX='http://' + BaseConfig.DISPATCHER_IP + ':' + BaseConfig.DISPATCHER_PORT
# PREFIX='http://' + 'localhost' + ':' + BaseConfig.DISPATCHER_PORT
# res = requests.post('http://' + BaseConfig.DISPATCHER_IP + ':' + BaseConfig.DISPATCHER_PORT + '/collector/imageinfo',
#                     json=total_info)

API={
    'imageinfo':'/collector/imageinfo',
    'starttime':'/collector/starttime'
}

for item in API:
    API[item]=PREFIX+API[item]

