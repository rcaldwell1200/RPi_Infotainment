#!/usr/bin/python
# -*- coding: utf-8 -*-
from Tkinter import *
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

        Label(frame, text='driver_Red').grid(row=0, column=0)
        Label(frame, text='driver_Green').grid(row=1, column=0)
        Label(frame, text='driver_Blue').grid(row=2, column=0)
        Label(frame, text='fPassenger_Red').grid(row=3, column=0)
        Label(frame, text='fPassenger_Green').grid(row=4, column=0)
        Label(frame, text='fPassenger_Blue').grid(row=5, column=0)
        Label(frame, text='lRPassenger_Red').grid(row=6, column=0)
        Label(frame, text='lRPassenger_Green').grid(row=7, column=0)
        Label(frame, text='lRPassenger_Blue').grid(row=8, column=0)
        Label(frame, text='rRPassenger_Red').grid(row=9, column=0)
        Label(frame, text='rRPassenger_Green').grid(row=10, column=0)
        Label(frame, text='rRPassenger_Blue').grid(row=11, column=0)
        scaledriver_Red = Scale(frame, from_=0, to=100,
                                orient=HORIZONTAL,
                                command=self.updatedriver_Red)
        scaledriver_Red.grid(row=0, column=1)
        scaledriver_Green = Scale(frame, from_=0, to=100,
                                  orient=HORIZONTAL,
                                  command=self.updatedriver_Green)
        scaledriver_Green.grid(row=1, column=1)
        scaledriver_Blue = Scale(frame, from_=0, to=100,
                                 orient=HORIZONTAL,
                                 command=self.updatedriver_Blue)
        scaledriver_Blue.grid(row=2, column=1)
        scalefPassenger_Red = Scale(frame, from_=0, to=100,
                                    orient=HORIZONTAL,
                                    command=self.updatefPassenger_Red)
        scalefPassenger_Red.grid(row=3, column=1)
        scalefPassenger_Green = Scale(frame, from_=0, to=100,
                orient=HORIZONTAL, command=self.updatefPassenger_Green)
        scalefPassenger_Green.grid(row=4, column=1)
        scalefPassenger_Blue = Scale(frame, from_=0, to=100,
                orient=HORIZONTAL, command=self.updatefPassenger_Blue)
        scalefPassenger_Blue.grid(row=5, column=1)
        scalelRPassenger_Red = Scale(frame, from_=0, to=100,
                orient=HORIZONTAL, command=self.updatelRPassenger_Red)
        scalelRPassenger_Red.grid(row=6, column=1)
        scalelRPassenger_Green = Scale(frame, from_=0, to=100,
                orient=HORIZONTAL, command=self.updatelRPassenger_Green)
        scalelRPassenger_Green.grid(row=7, column=1)
        scalelRPassenger_Blue = Scale(frame, from_=0, to=100,
                orient=HORIZONTAL, command=self.updatelRPassenger_Blue)
        scalelRPassenger_Blue.grid(row=8, column=1)
        scalerRPassenger_Red = Scale(frame, from_=0, to=100,
                orient=HORIZONTAL, command=self.updaterRPassenger_Red)
        scalerRPassenger_Red.grid(row=9, column=1)
        scalerRPassenger_Green = Scale(frame, from_=0, to=100,
                orient=HORIZONTAL, command=self.updaterRPassenger_Green)
        scalerRPassenger_Green.grid(row=10, column=1)
        scalerRPassenger_Blue = Scale(frame, from_=0, to=100,
                orient=HORIZONTAL, command=self.updaterRPassenger_Blue)
        scalerRPassenger_Blue.grid(row=11, column=1)

    def updatedriver_Red(self, duty):
        driver_Red.ChangeDutyCycle(float(duty))

    def updatedriver_Green(self, duty):
        driver_Green.ChangeDutyCycle(float(duty))

    def updatedriver_Blue(self, duty):
        driver_Blue.ChangeDutyCycle(float(duty))

    def updatefPassenger_Red(self, duty):
        fPassenger_Red.ChangeDutyCycle(float(duty))

    def updatefPassenger_Green(self, duty):
        fPassenger_Green.ChangeDutyCycle(float(duty))

    def updatefPassenger_Blue(self, duty):
        fPassenger_Blue.ChangeDutyCycle(float(duty))

    def updatelRPassenger_Red(self, duty):
        lRPassenger_Red.ChangeDutyCycle(float(duty))

    def updatelRPassenger_Green(self, duty):
        lRPassenger_Green.ChangeDutyCycle(float(duty))

    def updatelRPassenger_Blue(self, duty):
        lRPassenger_Blue.ChangeDutyCycle(float(duty))

    def updaterRPassenger_Red(self, duty):
        rRPassenger_Red.ChangeDutyCycle(float(duty))

    def updaterRPassenger_Green(self, duty):
        rRPassenger_Green.ChangeDutyCycle(float(duty))

    def updaterRPassenger_Blue(self, duty):
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

			