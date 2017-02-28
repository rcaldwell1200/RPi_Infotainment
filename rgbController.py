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
GPIO.setup(13, GPIO.OUT)
GPIO.setup(14, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)

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

# Trunk

lTrunk_Red = GPIO.PWM(13, 500)
lTrunk_Green = GPIO.PWM(14, 500)
lTrunk_Blue = GPIO.PWM(15, 500)

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

        buttondriver = Button(text='Driver Color',
                              command=self.updatedriver).pack()
        buttonfpassenger = Button(text='Passenger Color',
                                  command=self.updatefPassenger).pack()
        buttonlrpassenger = Button(text='L RPassenger',
                                   command=self.updatelRPassenger).pack()
        buttonrrpassenger = Button(text='R RPassenger',
                                   command=self.updaterRPassenger).pack()
        buttonltrunk = Button(text='Trunk',
                              command=self.updateTrunk).pack()

    def updatedriver(useless):
        color = askcolor()
        rgb = color[0]
        driver_Red.ChangeDutyCycle(float(rgb[0] / 2.56))
        driver_Green.ChangeDutyCycle(float(rgb[1] / 2.56))
        driver_Blue.ChangeDutyCycle(float(rgb[2] / 2.56))

    def updatefPassenger(useless):
        color = askcolor()
        rgb = color[0]
        fPassenger_Red.ChangeDutyCycle(float(rgb[0] / 2.56))
        fPassenger_Green.ChangeDutyCycle(float(rgb[1] / 2.56))
        fPassenger_Blue.ChangeDutyCycle(float(rgb[2] / 2.56))

    def updatelRPassenger(useless):
        color = askcolor()
        rgb = color[0]
        lRPassenger_Red.ChangeDutyCycle(float(rgb[0] / 2.56))
        lRPassenger_Green.ChangeDutyCycle(float(rgb[1] / 2.56))
        lRPassenger_Blue.ChangeDutyCycle(float(rgb[2] / 2.56))

    def updaterRPassenger(useless):
        color = askcolor()
        rgb = color[0]
        rRPassenger_Red.ChangeDutyCycle(float(rgb[0] / 2.56))
        rRPassenger_Green.ChangeDutyCycle(float(rgb[1] / 2.56))
        rRPassenger_Blue.ChangeDutyCycle(float(rgb[2] / 2.56))

    def updateTrunk(useless):
        color = askcolor()
        rgb = color[0]
        lTrunk_Red.ChangeDutyCycle(float(rgb[0] / 2.56))
        lTrunk_Green.ChangeDutyCycle(float(rgb[1] / 2.56))
        lTrunk_Blue.ChangeDutyCycle(float(rgb[2] / 2.56))


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

			