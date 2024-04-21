import BaseConfig

PREFIX='http://' + BaseConfig.DETECTOR_IP + ':' + BaseConfig.DETECTOR_PORT+'/'

API={
    'changeconfig':'detect/changeconfig'
}

for item in API:
    API[item]=PREFIX+API[item]