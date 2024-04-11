import BaseConfig

PREFIX='http://' + BaseConfig.DISPATCHER_IP + ':' + BaseConfig.DISPATCHER_PORT

API={
    'estimateinfo':'/collector/estimateinfo',
    'endtime':'/collector/endtime'
}

for item in API:
    API[item]=PREFIX+API[item]

