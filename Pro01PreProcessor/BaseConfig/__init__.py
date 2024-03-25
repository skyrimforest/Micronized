import os

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)),'..'))

RMQ_IP='10.30.0.1'
DISPATCHER_IP='10.30.0.4'
DISPATCHER_PORT='12003'
RMQ_USER='skyrim'
RMQ_PASS='111111'
RMQ_QUEUE='afterpreprocess'
RMQ_PORT=5672

OWN_PORT=12000

LOG_PATH=ROOT_DIR+'/loginfo'
PIC_INPUT_PATH=ROOT_DIR+'/inputpics'
VID_INPUT_PATH=ROOT_DIR+'/inputvideo'
OUTPUT_PATH=ROOT_DIR+'/outputpics'

