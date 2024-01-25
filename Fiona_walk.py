from adafruit_servokit import ServoKit
import time 
# default is 90. 
# to become loose use angle = None

# last (shoulder): - is left, + is right
# middle on: up is -, down is + degrees
# first (feet): up is -, down is + degrees

# move leg i to the side
# the second and third servo from the legs are needed

def initialize_servos(kit, kit2):
    for i in range(16):
        kit.servo[i].angle = 90
    for i in range(3):
        kit2.servo[i].angle = 90
    
def loose_servos(kit, kit2):
    for i in range(16):
        kit.servo[i].angle = None
    for i in range(3):
        kit2.servo[i].angle = None

# move servo from 90 by an amount of degrees
# getting it back to 90, set degrees to 0
# example: move 30 degrees up = 90 - 30 = 60, or 90 + 30 = 120 for the other side
def move(servo, degrees, kit = ServoKit(channels=16), kit2 = ServoKit(channels=16, address=0x50)):
    if servo in [3,4,5,9,10,11,15,16,17] :
        angle = 90 + degrees
    else:
        angle = 90 - degrees

    if servo <= 14:
        kit.servo[servo].angle = angle
    else:
        servo = servo - 15
        kit2.servo[servo].angle = angle

