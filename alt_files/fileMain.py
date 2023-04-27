import RPi.GPIO as GPIO
#from EmulatorGUI import GPIO
import time
import requests
import Hx711

# Define the sensor pins
PIN_DOUT = 21
PIN_SLK = 23

# Define the weight threshold in grams
WEIGHT_THRESHOLD = 1000

# Set up GPIO pins
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN_DOUT, GPIO.IN)
GPIO.setup(PIN_SLK, GPIO.OUT)
GPIO.output(PIN_SLK, GPIO.LOW)
time.sleep(0.1)
GPIO.output(PIN_SLK, GPIO.HIGH)
GPIO.setup(PIN_DOUT, GPIO.IN)

# Create an instance of Hx711 class
hx711 = Hx711(PIN_DOUT, PIN_SLK)

try:
    while True:
        # Get the weight in grams from the motorCode sensor
        weight = hx711.getGram()

        # Check if the weight has reached the threshold
        if weight <= WEIGHT_THRESHOLD:
            print("Weight threshold reached: {} grams".format(weight))

            # Send a signal to the web server
            #payload = {"weight": weight}
            sigCode = {"Signal": 1}
            
            #response = requests.post("http://example.com/endpoint", data=sigCode)

            """if response.status_code == 200:
                print("Signal sent successfully")
            else:
                print("Failed to send signal: {}".format(response.status_code))"""

        
        
        else:
            # Send a signal to the web server
            print("Weight not reached. {}".format(weight))
            #payload = {"weight": weight}
            sigCode = {"Signal": 0}
            
            #response = requests.post("http://example.com/endpoint", data=sigCode)

            """if response.status_code == 200:
                print("Signal sent successfully")
            else:
                print("Failed to send signal: {}".format(response.status_code))"""
        
        time.sleep(1)

except KeyboardInterrupt:
    pass

finally:
    # Clean up GPIO pins
    GPIO.cleanup()
