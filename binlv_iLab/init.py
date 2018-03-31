import RPi.GPIO as GPIO
import time

beef_pin = 35

def init():
	GPIO.setwarnings(False)
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(beef_pin,GPIO.OUT)
	GPIO.output(beef_pin,GPIO.HIGH)
	pass

init()
time.sleep(2)
GPIO.cleanup()
