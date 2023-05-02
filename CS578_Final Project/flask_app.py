from flask import Flask, jsonify, request, render_template
import RPi.GPIO as GPIO
import time
from hx711 import HX711

app = Flask(__name__)

GPIO.setmode(GPIO.BCM)
PIN_DOUT = 10
PIN_SLK = 11

PIN_IN1 = 26
PIN_IN2 = 19
PIN_EN = 6

GPIO.setup(PIN_IN1, GPIO.OUT)
GPIO.setup(PIN_IN2, GPIO.OUT)
GPIO.setup(PIN_EN, GPIO.OUT)
power_a = GPIO.PWM(PIN_EN, 100)
#power_a.start(0)
power_a.stop()
	
referenceUnit = 472.7
hx = HX711(PIN_DOUT, PIN_SLK) #may need a enable input similar to motorCode
hx.set_reading_format("MSB", "MSB")
hx.set_reference_unit(referenceUnit)
hx.reset()
hx.tare()

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/device-data')
def gpio_data():
	
	weight = hx.get_weight(5)
	send_data = {
		'weight': "{:.1f} grams".format(weight),
		'status': " "
	}
	if weight <= 25:
		send_data['status'] = "Bowl is near empty"
		GPIO.output(PIN_IN1, GPIO.HIGH)
		GPIO.output(PIN_IN2, GPIO.LOW)
		GPIO.output(PIN_EN, GPIO.HIGH)
		time.sleep(10)
		GPIO.output(PIN_IN1, GPIO.LOW)
		GPIO.output(PIN_IN2, GPIO.LOW)
		GPIO.output(PIN_EN, GPIO.LOW)
		
	else:
		send_data['status'] = "Bowl is near full"
		
	return render_template('device_data.html', data= send_data)

	
	
@app.route('/update_value')
def update_value():
	weight = hx.get_weight(5)
	print(weight)
	send_data = {
		'weight': "{:.1f} grams".format(weight),
		'status': " "
	}
	if weight <= 25:
		send_data['status'] = "Bowl is near empty"
		GPIO.output(PIN_IN1, GPIO.HIGH)
		GPIO.output(PIN_IN2, GPIO.LOW)
		GPIO.output(PIN_EN, GPIO.HIGH)
		time.sleep(5)
		GPIO.output(PIN_IN1, GPIO.LOW)
		GPIO.output(PIN_IN2, GPIO.LOW)
		GPIO.output(PIN_EN, GPIO.LOW)
		
	else:	
		send_data['status'] = "Bowl is near full"
		
	return jsonify(updated_value=send_data)
	
@app.route('/setup')
def device_setup():
	return render_template('setup.html')
	
@app.route('/signup')
def signup_form():
	return render_template('signup.html')
	
@app.route('/login')
def login_form():
	return render_template('login.html')
	
@app.route('/statistics')
def show_stats():
	return render_template('statistics.html')

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')
