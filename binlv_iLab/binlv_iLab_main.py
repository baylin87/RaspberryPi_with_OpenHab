import RPi.GPIO as GPIO
import time
import os
import dayu

beef_pin = 35
detct_pin = 12

def init():
	GPIO.setwarnings(False)
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(detct_pin,GPIO.IN)
	GPIO.setup(beef_pin,GPIO.OUT)
	pass

def beep():
	while GPIO.input(detct_pin):
		GPIO.output(beef_pin,GPIO.HIGH)
		time.sleep(0.5)
		GPIO.output(beef_pin,GPIO.LOW)
		time.sleep(0.5)

def detct():
	for i in range(1,7):
		if GPIO.input(detct_pin) == True:
			print "Someone is closing!"
			beep()
			dayu.dayu_tt("18256021703","SMS_70185251")
			#os.system('/home/pi/Documents/binlv_iLab/yeelink.sh')
		else:
			GPIO.output(beef_pin,GPIO.HIGH)
			print "Noanybody!"
		time.sleep(2)

init()
detct()
#GPIO.cleanup()
