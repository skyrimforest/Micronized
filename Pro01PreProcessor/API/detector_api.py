import BaseConfig

PREFIX='http://' + BaseConfig.DETECTOR_IP + ':' + BaseConfig.DETECTOR_PORT

API={
    'recvdetect':'/detect/recvdetect',
    'recvdetectcpu':'/detect/recvdetectcpu'
}

for item in API:
    API[item]=PREFIX+API[item]