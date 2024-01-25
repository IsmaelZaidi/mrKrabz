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
        kit2.servo[servo - 15].angle = angle

# do x amount of steps for this walk cycle
def walk(x):
    for i in range(x):
        # set 1 up
        move(1, 30)
        move(10, 30)
        move(13, 30)
        time.sleep(0.5)
        # push set 2
        move(5, -20)
        move(8, -20)
        move(17, -20)
        time.sleep(0.5)
        # set 1 down
        move(1, 0)
        move(10, 0)
        move(13, 0)
        # set 2 up and place in middle
        move(4, 30)
        move(7, 30)
        move(16, 30)
        time.sleep(0.5)
        move(5, 0)
        move(8, 0)
        move(17, 0)
        # push set 1
        move(2, -20)
        move(11, -20)
        move(14, -20)
        # set 2 down
        move(4, 0)
        move(7, 0)
        move(16, 0)
        # place set 1 in middle
        move(1, 30)
        move(10, 30)
        move(13, 30)
        time.sleep(0.5)
        move(2, 0)
        move(11, 0)
        move(14, 0)
        # skip this step en repeat for continous walking
        time.sleep(0.5)
        move(1, 0)
        move(10, 0)
        move(13, 0)





kit = ServoKit(channels=16)
kit2 = ServoKit(channels=16, address=0x50)

initialize_servos(kit, kit2)

loose_servos(kit, kit2)