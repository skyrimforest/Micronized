import os

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)),'..'))

# RMQ_IP='10.30.0.5'
RMQ_IP='localhost'
# DISPATCHER_IP='10.30.0.4'
DISPATCHER_IP='localhost'
DISPATCHER_PORT='12003'
RMQ_USER='skyrim'
RMQ_PASS='111111'
RMQ_QUEUE_RECV='afterfacedetect'
RMQ_QUEUE_FORWARD='afterestimate'
RMQ_PORT=5672

OWN_PORT=12002

LOG_PATH=ROOT_DIR+'/loginfo'
OUT_PATH=ROOT_DIR+'/output'
