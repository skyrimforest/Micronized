import BaseConfig

PREFIX='http://' + BaseConfig.ESTIMATOR_IP + ':' + BaseConfig.ESTIMATOR_PORT


API={
    'recvestimate': '/estimate/draw',
    'setestimate': '/estimate/sex'
}

for item in API:
    API[item]=PREFIX+API[item]