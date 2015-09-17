import RPi.GPIO as GPIO
import lirc
import time
import os

#Pin assignments for various signals, following BCM convention
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)		#disable warnings
mot1en = 17
mot1plus = 27
mot1minus = 22
mot2en = 3
mot2plus = 4
mot2minus = 2

allpins = [mot1en, mot1plus, mot1minus, mot2en, mot2plus, mot2minus]

GPIO.setup(allpins, GPIO.OUT)

def stop():
	''' Just cuts all power to motors'''
	GPIO.output(allpins, 0)

def forward(delay):
	''' Moves motors forward for delay seconds'''
	GPIO.output([mot1en, mot1minus, mot2en, mot2plus], 1)
	time.sleep(delay)
	stop()

def backward(delay):
	''' Moves motors backward for delay seconds'''
	GPIO.output([mot1en, mot1plus, mot2en, mot2minus], 1)
	time.sleep(delay)
	stop()

def left(delay):
	''' Moves motors to the left for delay seconds'''
	GPIO.output([mot1en, mot1minus, mot2en, mot2minus], 1)
	time.sleep(delay)
	stop()

def right(delay):
	''' Moves motors to the right for delay seconds'''
	GPIO.output([mot1en, mot1plus, mot2en, mot2plus], 1)
	time.sleep(delay)
	stop()
	
if __name__ == '__main__':
	stop()
	#I'm alive
	forward(2)
	backward(2)
	left(2)
	right(2)
	
	#Start grabbing information from LIRC
	sockid = lirc.init("myprogram", blocking = False)
	
	while True:
		result = lirc.nextcode()		#Returns a list
		if result == []:			#Check for empty list
			command = 'empty'
		else:
			command = result[0]
		
		if command == 'forward':
			forward(0.5)
		elif command == 'back':
			backward(0.5)
		elif command == 'left':
			left(0.5)
		elif command == 'right':
			right(0.5)
		elif command == 'power':
			break
		else:
			continue
	lirc.deinit()
	os.system('shutdown now')

	
	

