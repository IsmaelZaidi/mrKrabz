import time
from adafruit_servokit import ServoKit

def initialize_servo_kits(channels_per_kit=16, kit1_address=None, kit2_address=None):
    # Initialize the first servo kit (default I2C address if not provided)
    kit1 = ServoKit(channels=channels_per_kit, address=kit1_address)

    # Initialize the second servo kit with a specified I2C address (or default if not provided)
    kit2 = ServoKit(channels=channels_per_kit, address=kit2_address)

    return kit1, kit2

def move_servos(kit, channel, angle):
    # Move a specific servo to a specified angle
    kit.servo[channel].angle = angle
    time.sleep(0.1)  # Add a delay for the servo to reach the position

def forward_movement(kit1, kit2):
    # Define the channels for the femur and tibia of each leg
    leg_channels = [(1, 2), (4, 5), (7, 8), (10, 11), (13, 14), (16, 17)]  # Update these as per your setup

    # Move each leg
    for femur_channel, tibia_channel in leg_channels:
        # Lift the leg
        move_servos(kit1, femur_channel, 130) 
        time.sleep(0.5)
        # Move forward
        move_servos(kit1, tibia_channel, 45)
        time.sleep(0.5)
        # Move leg back down
        move_servos(kit1, femur_channel, 90) 
        time.sleep(0.5)
        # Move shoulder back to 90 degrees
        move_servos(kit1, tibia_channel, 90)
        time.sleep(0.5)


def main():
    # Set the desired I2C addresses for the servo kits
    kit1_address = 0x40  # Use default I2C address for kit1
    kit2_address = 0x50  # Specify I2C address for kit2

    # Initialize servo kits
    kit1, kit2 = initialize_servo_kits(kit1_address=kit1_address, kit2_address=kit2_address)

    try:
        # Set the angle for each servo to 90 degrees on both controllers
        for i in range(16):
            kit1.servo[i].angle = 90

        # Set specific angles for servos on kit2
        kit2.servo[0].angle = 90
        kit2.servo[1].angle = 90
        kit2.servo[2].angle = 90

        # Add any additional operations or delays here
        time.sleep(5)
        forward_movement(kit1, kit2)

    finally:
        # Release resources
        kit1.deinit()
        kit2.deinit()

if __name__ == "__main__":
    main()
