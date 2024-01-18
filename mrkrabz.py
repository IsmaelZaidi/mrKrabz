import time
from adafruit_servokit import ServoKit

class MrKrabz:
    def __init__(self, channels_per_kit=16):
        self.kits = self.initialize_servo_kits(channels_per_kit)
        self.legs = {
            "leg1": {"kit": "kit1", "coxa": 0, "femur": 1, "tibia": 2},
            "leg2": {"kit": "kit1", "coxa": 3, "femur": 4, "tibia": 5},
            "leg3": {"kit": "kit1", "coxa": 6, "femur": 7, "tibia": 8},
            "leg4": {"kit": "kit1", "coxa": 9, "femur": 10, "tibia": 11},
            "leg5": {"kit": "kit1", "coxa": 12, "femur": 13, "tibia": 14},
            "leg6": {"kit": "kit2", "coxa": 0, "femur": 1, "tibia": 2},
        }

    def initialize_servo_kits(self, channels_per_kit):
        # Initialize the first servo kit with I2C address 0x40
        kit1 = ServoKit(channels=channels_per_kit, address=0x40)

        # Initialize the second servo kit with I2C address 0x50
        kit2 = ServoKit(channels=channels_per_kit, address=0x50)

        return {"kit1": kit1, "kit2": kit2}

    def move(self, leg_name, part_name, angle):
        kit_name = self.legs[leg_name]["kit"]
        channel = self.legs[leg_name][part_name]
        self.kits[kit_name].servo[channel].angle = angle
        time.sleep(0.1)  # Add a delay for the servo to reach the position

def main():
    mrkrabz = MrKrabz()

    # Put all angles for every leg at 90 degrees
    for leg_name in mrkrabz.legs:
        for part_name in ["coxa", "femur", "tibia"]:
            mrkrabz.move(leg_name, part_name, 90)

    # Lift leg 1, 3 and 5 up
    mrkrabz.move("leg1", "femur", 130)
    mrkrabz.move("leg3", "femur", 130)
    mrkrabz.move("leg5", "femur", 130)

    #work on this later


if __name__ == "__main__":
    main()            