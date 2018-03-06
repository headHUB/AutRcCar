"""Configurations for the RC car"""

PICAMERA_RESOLUTION = (640,480)
PICAMERA_FRAMERATE = 60
PICAMERA_WARM_UP_TIME = 2

BACK_MOTOR_DATA_ONE = 17
BACK_MOTOR_DATA_TWO = 27
BACK_MOTOR_ENABLE_PIN = 22
FRONT_MOTOR_DATA_ONE = 19
FRONT_MOTOR_DATA_TWO = 26
PWM_FREQUENCY = 1000
INITIAL_PWM_DUTY_CYCLE = 100

CLASSIFICATION_LABELS = ['forward', 'reverse', 'left', 'right', 'idle']
CLASSIFICATION_LABELS_AND_VALUES = {
    'forward': [1, 0, 0, 0, 0],
    'reverse': [0, 1, 0, 0, 0],
    'left': [0, 0, 1, 0, 0],
    'right': [0, 0, 0, 1, 0],
    'idle': [0, 0, 0, 0, 1]
}


IMAGE_DIMENSIONS = (75, 75)
LAMBDA = 0.0
HIDDEN_LAYER_SIZE = 50
