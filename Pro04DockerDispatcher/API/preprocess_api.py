import BaseConfig

PREFIX='http://' + BaseConfig.PREPROCESSOR_IP + ':' + BaseConfig.PREPROCESSOR_PORT+'/'

API={
    'changeconfig':'video/changeconfig',
}

for item in API:
    API[item]=PREFIX+API[item]