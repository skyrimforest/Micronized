import os

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)),'..'))

RMQ_IP='192.168.227.129'
RMQ_USER='skyrim'
RMQ_PASS='111111'
RMQ_QUEUE='dockerdispatcher'
RMQ_PORT=5672

OWN_PORT=12000

LOG_PATH=ROOT_DIR+'/loginfo'
INPUT_PATH=ROOT_DIR+'/inputpics'
OUTPUT_PATH=ROOT_DIR+'/outputpics'
DB_PATH=ROOT_DIR+'/dboperator'