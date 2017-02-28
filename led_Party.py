import RPi.GPIO as GPIO
import random
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
led1 = GPIO.PWM(18, 100)
led2 = GPIO.PWM(12, 100)
led3 = GPIO.PWM(13, 100)
led1.start(100)
led2.start(100)
led3.start(100)
while True:
	led1.ChangeDutyCycle(random.randint(0,100))
	led2.ChangeDutyCycle(random.randint(0,100))
	led3.ChangeDutyCycle(random.randint(0,100))
	time.sleep(0.10)