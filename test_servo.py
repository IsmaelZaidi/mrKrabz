
import adafruit_servokit

def set_servo_angle(servo, angle):
    kit = adafruit_servokit.ServoKit(channels=16)
    kit.servo[servo].angle = angle

# Example usage:
set_servo_angle(0, 90)  # Set servo 0 to 90 degrees
