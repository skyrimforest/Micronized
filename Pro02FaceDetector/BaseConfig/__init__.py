import os

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)),'..'))

RMQ_IP='192.168.227.129'
DISPATCHER_IP='localhost'
DISPATCHER_PORT='12003'
RMQ_USER='skyrim'
RMQ_PASS='111111'
RMQ_QUEUE_RECV='afterpreprocess'
RMQ_QUEUE_FORWARD='afterfacedetect'
RMQ_PORT=5672

OWN_PORT=12001

LOG_PATH=ROOT_DIR+'/loginfo'

