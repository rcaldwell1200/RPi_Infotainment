#!/usr/bin/python
# -*- coding: utf-8 -*-
from Tkinter import *
from tkColorChooser import askcolor
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Setup pins here

GPIO.setup(1, GPIO.OUT)
GPIO.setup(2, GPIO.OUT)
GPIO.setup(3, GPIO.OUT)
GPIO.setup(4, GPIO.OUT)
GPIO.setup(5, GPIO.OUT)
GPIO.setup(6, GPIO.OUT)
GPIO.setup(7, GPIO.OUT)
GPIO.setup(8, GPIO.OUT)
GPIO.setup(9, GPIO.OUT)
GPIO.setup(10, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)

# Define pins and profiles
# Driver

driver_Red = GPIO.PWM(1, 500)
driver_Green = GPIO.PWM(2, 500)
driver_Blue = GPIO.PWM(3, 500)

# FrontPassenger

fPassenger_Red = GPIO.PWM(4, 500)
fPassenger_Green = GPIO.PWM(5, 500)
fPassenger_Blue = GPIO.PWM(6, 500)

# LeftRPassenger

lRPassenger_Red = GPIO.PWM(7, 500)
lRPassenger_Green = GPIO.PWM(8, 500)
lRPassenger_Blue = GPIO.PWM(9, 500)

# RightRPassenger

rRPassenger_Red = GPIO.PWM(10, 500)
rRPassenger_Green = GPIO.PWM(11, 500)
rRPassenger_Blue = GPIO.PWM(12, 500)

# Start PWM

driver_Red.start(50)
driver_Green.start(50)
driver_Blue.start(50)
fPassenger_Red.start(50)
fPassenger_Green.start(50)
fPassenger_Blue.start(50)
lRPassenger_Red.start(50)
lRPassenger_Green.start(50)
lRPassenger_Blue.start(50)
rRPassenger_Red.start(50)
rRPassenger_Green.start(50)
rRPassenger_Blue.start(50)

# Set Default Values
# Not really sure how thats gonna happen

# create gui code

class App:

    def __init__(self, master):
        frame = Frame(master)
        frame.pack()

        # Labels and positions


        buttondriver = Button(text='Driver Color', command=self.updatedriver).pack()
	buttonfpassenger = Button(text='Passenger Color', command=self.updatefPassenger).pack()
	buttonlrpassenger = Button(text='L RPassenger', command=self.updatelRPassenger).pack()
	buttonrrpassenger = Button(text='R RPassenger', command=self.updaterRPassenger).pack()


    def updatedriver(useless):
	color = askcolor()
	rgb = color[0]
        driver_Red.ChangeDutyCycle(float(rgb[0] / 2.56))
	driver_Green.ChangeDutyCycle(float(rgb[1] / 2.56))
	driver_Blue.ChangeDutyCycle(float(rgb[2] / 2.56))

    def updatefPassenger(useless):
        fPassenger_Red.ChangeDutyCycle(float(duty))
        fPassenger_Green.ChangeDutyCycle(float(duty))
        fPassenger_Blue.ChangeDutyCycle(float(duty))

    def updatelRPassenger(self, duty):
        lRPassenger_Red.ChangeDutyCycle(float(duty))
        lRPassenger_Green.ChangeDutyCycle(float(duty))
        lRPassenger_Blue.ChangeDutyCycle(float(duty))

    def updaterRPassenger(self, duty):
        rRPassenger_Red.ChangeDutyCycle(float(duty))
        rRPassenger_Green.ChangeDutyCycle(float(duty))
        rRPassenger_Blue.ChangeDutyCycle(float(duty))


# Set the GUI running, give the window a title, size and position

root = Tk()
root.wm_title('RGB LED Control')
app = App(root)
root.geometry('500x500+0+0')
try:
    root.mainloop()
finally:
    print 'Cleaning up'
GPIO.cleanup()

			