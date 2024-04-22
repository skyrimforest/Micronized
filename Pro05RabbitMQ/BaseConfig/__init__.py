import os

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)),'..'))

CLOUD_IP='localhost'
EDGE_IP='localhost'

# DISPATCHER_IP='10.30.0.4'
PREPROCESSOR_IP=CLOUD_IP
PREPROCESSOR_PORT='12000'
DETECTOR_IP=CLOUD_IP
DETECTOR_PORT='12001'
ESTIMATOR_IP=CLOUD_IP
ESTIMATOR_PORT='12002'
DISPATCHER_IP=CLOUD_IP
DISPATCHER_PORT='12003'
NET_IP=CLOUD_IP
NET_PORT='12004'

OAKESTRA_IP='192.168.227.133'
OAKESTRA_PORT='10000'
OAKESTRA_USERNAME='Admin'
OAKESTRA_PASSWORD='Admin'
APPLICATION_ID=''
SERVICE_ID=''


LOG_PATH=ROOT_DIR+'/loginfo'
PIC_INPUT_PATH=ROOT_DIR+'/inputpics'
VID_INPUT_PATH=ROOT_DIR+'/inputvideo'
OUTPUT_PATH=ROOT_DIR+'/outputpics'
DB_PATH=ROOT_DIR+'/dboperator'