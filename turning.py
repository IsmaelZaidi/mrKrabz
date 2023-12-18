from adafruit_servokit import ServoKit
kit = ServoKit(channels=18)

# default is 90. 
# to become loose use angle = None

# move leg i to the side
# the second and third servo from the legs are needed
def move_leg(i):
    n1 = i*3 + 1
    n2 = i*3 + 2
    kit.servo[n1].angle = 60
    kit.servo[n2].angle = 45
    time.sleep(0.3)
    kit.servo[n1].angle = 90

move_leg(0)