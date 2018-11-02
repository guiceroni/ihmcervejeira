import RPi.GPIO as GPIO

def inicio():
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(6, GPIO.OUT)
	GPIO.output(6, GPIO.LOW)
	GPIO.setup(13, GPIO.OUT)
	GPIO.output(13, GPIO.LOW)
	GPIO.setup(20, GPIO.OUT)
	GPIO.output(20, GPIO.LOW)
	GPIO.setup(26, GPIO.OUT)
	GPIO.output(26, GPIO.LOW)
	GPIO.setup(21, GPIO.OUT)
	GPIO.output(21, GPIO.LOW)
	GPIO.setup(22, GPIO.OUT)
	GPIO.output(22, GPIO.LOW)
	GPIO.setup(16, GPIO.IN)
	GPIO.setup(19, GPIO.IN)
	GPIO.setup(12, GPIO.IN)
    

