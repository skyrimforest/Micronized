import BaseConfig

PREFIX='http://' + BaseConfig.DETECTOR_IP + ':' + BaseConfig.DETECTOR_PORT+'/'

API={
    'login':'auth/login',
    'appreg':'application',
    'serdeploy':'service',
    'clustersinfo':'clusters/active'
}

for item in API:
    API[item]=PREFIX+API[item]