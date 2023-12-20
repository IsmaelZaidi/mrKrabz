
import adafruit_servokit

def set_servo_angle(servo, angle):
    kit = adafruit_servokit.ServoKit(channels=16)
    kit.servo[servo].actuation_range = 180  # Set the range of motion to 180 degrees
    kit.servo[servo].set_pulse_width_range(500, 2500)  # Set pulse width range for SG90 servo
    kit.servo[servo].frequency = 50  # Set the PWM frequency to 50 Hz

    kit.servo[servo].angle = angle

# Example usage:
set_servo_angle(0, 90)  # Set servo 0 to 90 degrees
