import os

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)),'..'))

# DISPATCHER_IP='10.30.0.4'
PREPROCESSOR_IP='localhost'
PREPROCESSOR_PORT='12000'
DETECTOR_IP='localhost'
DETECTOR_PORT='12001'
ESTIMATOR_IP='localhost'
ESTIMATOR_PORT='12002'
DISPATCHER_IP='localhost'
DISPATCHER_PORT='12003'

LOG_PATH=ROOT_DIR+'/loginfo'
PIC_INPUT_PATH=ROOT_DIR+'/inputpics'
VID_INPUT_PATH=ROOT_DIR+'/inputvideo'
OUTPUT_PATH=ROOT_DIR+'/outputpics'

