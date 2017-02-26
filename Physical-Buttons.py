import RPi.GPIO as GPIO
import time
import os
GPIO.setmode(GPIO.BCM)

#SETUP PINS
#Last
GPIO.setup(17,GPIO.IN)
#Play
GPIO.setup(27,GPIO.IN)
#Next
GPIO.setup(22,GPIO.IN)
#Volume dn 
GPIO.setup(18,GPIO.IN)
#Volume up 
GPIO.setup(23,GPIO.IN)

#define prev values so python doesn't explode
input_Last_prev = 0
input_Play_prev = 0
input_Next_prev = 0
input_VlDn_prev = 0
input_VlUp_prev = 0

#Main Application
while True:
	#take reading of pins
	input_Last = GPIO.input(17)
	input_Play = GPIO.input(27)
	input_Next = GPIO.input(22)
	input_VlDn = GPIO.input(18)
	input_VlUp = GPIO.input(23)
	
	#do action if pin has been pressed
	if ((not input_Last_prev) and input_Last):
		os.system("xdotool key F7")
	if ((not input_Play_prev) and input_Play):
		os.system("xdotool key F8")
	if ((not input_Next_prev) and input_Next):
		os.system("xdotool key F9")
	if ((not input_VlDn_prev) and input_VlDn):
		os.system("xdotool key F10")
	if ((not input_VlUp_prev) and input_VlUp):
		os.system("xdotool key F11")
	
	#Set pin previous values
	input_Last_prev = input_Last
	input_Play_prev = input_Play
	input_Next_prev = input_Next
	input_VlDn_prev = input_VlDn
	input_VlUp_prev = input_VlUp
	#debounce
	time.sleep(0.05)

