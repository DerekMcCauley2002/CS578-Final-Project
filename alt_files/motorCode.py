import RPi.GPIO as GPIO
import time

# Define motor pins
PIN_IN1 = 17
PIN_IN2 = 18
PIN_EN = 19

# Set up GPIO pins
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN_IN1, GPIO.OUT)
GPIO.setup(PIN_IN2, GPIO.OUT)
GPIO.setup(PIN_EN, GPIO.OUT)

# Set initial motor state
GPIO.output(PIN_IN1, GPIO.LOW)
GPIO.output(PIN_IN2, GPIO.LOW)
GPIO.output(PIN_EN, GPIO.LOW)

# Function to drive motor forward
def motor_forward():
    GPIO.output(PIN_IN1, GPIO.HIGH)
    GPIO.output(PIN_IN2, GPIO.LOW)
    GPIO.output(PIN_EN, GPIO.HIGH)

# Function to drive motor backward
def motor_backward():
    GPIO.output(PIN_IN1, GPIO.LOW)
    GPIO.output(PIN_IN2, GPIO.HIGH)
    GPIO.output(PIN_EN, GPIO.HIGH)

# Function to stop motor
def motor_stop():
    GPIO.output(PIN_IN1, GPIO.LOW)
    GPIO.output(PIN_IN2, GPIO.LOW)
    GPIO.output(PIN_EN, GPIO.LOW)

try:
    # Drive motor forward for 3 seconds
    motor_forward()
    print("Motor Forward")
    time.sleep(3)

    # Drive motor backward for 3 seconds
    motor_backward()
    print("Motor Backward")
    time.sleep(3)

    # Stop motor for 3 seconds
    motor_stop()
    print("Motor Stop")
    time.sleep(3)

except KeyboardInterrupt:
    pass

finally:
    # Clean up GPIO pins
    GPIO.cleanup()
