from adafruit_servokit import ServoKit
import time 
# default is 90. 
# to become loose use angle = None

# middle on: up is -, down is + degrees
# last (shoulder): 
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

def move_leg(i):

    # get servo number
    n1 = i*3 + 1
    n2 = i*3 + 2
    # move leg up and to the side
    kit.servo[n1].angle = 60
    kit.servo[n2].angle = 45
    # wait, then put leg down
    time.sleep(0.3)
    kit.servo[n1].angle = 90

# make a turn of 45 degrees
def turn_45(kit, kit2):
    # lift set1 up
    kit.servo[1].angle = 60
    kit.servo[13].angle = 60
    kit.servo[10].angle = 120
    time.sleep(1)

    # turn with set 2
   # kit.servo[5].angle = 45
    kit.servo[8].angle = 135
    kit2.servo[2].angle = 45
    time.sleep(1)

    # put set1 down
 #   kit.servo[2].angle = 135
  #  kit.servo[14].angle = 135
   # kit.servo[11].angle = 45
    time.sleep(1)
    kit.servo[1].angle = 90
    kit.servo[13].angle = 90
    kit.servo[10].angle = 90

    # lift, move and put down set 2
    kit.servo[4].angle = 120
    kit.servo[7].angle = 60
    kit2.servo[1].angle = 120
    time.sleep(1)
    #kit.servo[5].angle = 90
    kit.servo[8].angle = 90
    kit2.servo[2].angle = 90
    time.sleep(1)
    kit.servo[4].angle = 90
    kit.servo[7].angle = 90
    kit2.servo[1].angle = 90


kit = ServoKit(channels=16)
kit2 = ServoKit(channels=16, address=0x50)
initialize_servos(kit, kit2)


turn_45(kit, kit2)

loose_servos(kit, kit2)