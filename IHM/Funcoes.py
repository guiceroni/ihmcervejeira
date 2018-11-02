import RPi.GPIO as pin
import time

def Liga(x):
    pin.output(x, pin.HIGH)
    
def Desliga(x):
    pin.output(x, pin.LOW)
    
def Le(x):
    return pin.input(x)
    
def PassoF():
	pin.output(21, pin.HIGH)
	time.sleep(0.1)
	pin.output(21, pin.LOW)
	
def PassoT():
	pin.output(26, pin.HIGH)
	time.sleep(0.1)
	pin.output(26, pin.LOW)
	
def Alarme():
	pin.output(22, pin.HIGH)
	time.sleep(0.1)
	pin.output(22, pin.LOW)
