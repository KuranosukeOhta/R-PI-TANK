# -*- coding: utf-8 -*-
"""
Created on Tue Jan  14 20:18:04 2020

@author: ohtak
"""

gpio_pin = 17
gpio_pin2 = 27
#1= left
#2= right
import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

GPIO.setup(gpio_pin , GPIO.OUT)
GPIO.setup(gpio_pin2 , GPIO.OUT)
#27 = right
def Right(none):
    GPIO.output(gpio_pin, 0)
    GPIO.output(gpio_pin2, 1)
    time.sleep(0.60)
    Off("a")
    return 0
def Left(none):
    GPIO.output(gpio_pin, 1)
    GPIO.output(gpio_pin2, 0)
    time.sleep(0.60)
    Off("a")
    return 0
def Straight(none):
    for i in range(2):
        Right(0)
        time.sleep(0.1)
        Off("r")
        Left(0)
        time.sleep(0.17)
        Off("l")
    return 0
def Off(which):
    if which == "r":
        GPIO.output(gpio_pin2 , 0)
    elif which == "l":
        GPIO.output(gpio_pin , 0)
    elif which == "a":
        GPIO.output(gpio_pin , 0)
        GPIO.output(gpio_pin2 , 0)
    return 0
while True:
    try:
        answer = ""
        answer = raw_input("Chose, s  or r  or l or ss or e.")
        if answer == "s":
            Straight(0)
        elif answer == "r":
            Right(0)
        elif answer == "l":
            Left(0)
        elif answer == "ss":
            Off("a")
        elif answer == "e":
            break
        else:
            print("What?")

    except KeyboardInterrupt:
        print("safe end.")
        break

GPIO.cleanup()
print("All end.")
