import BaseConfig

PREFIX='http://' + BaseConfig.ESTIMATOR_IP + ':' + BaseConfig.ESTIMATOR_PORT


API={
    'recvestimate': '/estimate/draw'
}

for item in API:
    API[item]=PREFIX+API[item]