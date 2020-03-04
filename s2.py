# -*- coding: utf-8 -*-
"""
Created on Tue Jan  14 20:18:04 2020

@author: ohtak
"""

gpio_pin = 17
gpio_pin2 = 27
#1= left
#2= right
import sys
import time
import cv2
import numpy as  np
import RPi.GPIO as GPIO
cap = cv2.VideoCapture(0)

GPIO.setmode(GPIO.BCM)

GPIO.setup(gpio_pin , GPIO.OUT)
GPIO.setup(gpio_pin2 , GPIO.OUT)
#27 = right
run_time = 0.1
def Right(none):
    GPIO.output(gpio_pin, 0)
    GPIO.output(gpio_pin2, 1)
    time.sleep(run_time)
    Off("a")
    return 0
def Left(none):
    GPIO.output(gpio_pin, 1)
    GPIO.output(gpio_pin2, 0)
    time.sleep(run_time)
    Off("a")
    return 0
def Straight(none):
    GPIO.output(gpio_pin, 1)
    GPIO.output(gpio_pin2, 1)
    time.sleep(run_time + 0.5)
    Off("a")
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


before = None
camera_mode = 3
while True:
    try:
        ret, frame = cap.read()
        if camera_mode == 2:
            cv2.imshow("camera", frame)
        else:
            gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
            if camera_mode == 1:
                if before is None:
                    before = gray.copy().astype("float")
                    continue
                cv2.imshow("camera", gray)

            else:

                #before = gray.copy().astype("float")

                #ret,two = cv2.threshold(gray,147,255,cv2.THRESH_BINARY)
                ret,two = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)
                cv2.imshow("camera", two)
                """
                cv2.accumulateWeighted(gray, before, 0.7)
                mdframe = cv2.absdiff(gray, cv2.convertScaleAbs(before))


                ret,thresh2 = cv2.threshold(mdframe,10,255,cv2.THRESH_BINARY)

                ret,thresh1 = cv2.threshold(gray,147,255,cv2.THRESH_BINARY)
                cv2.imshow("threshed1", thresh1)
                """





        k = cv2.waitKey(1)&0xff
        if k == ord("w"):
            print("w")
            Straight(0)
        elif k == ord("d"):
            print("r")
            Right(0)
        elif k == ord("a"):
            print("l")
            Left(0)
        elif k == ord("i"):
            run_time += 0.1
            print(run_time)
            print("Straight" , str(run_time + 0.5))
        elif k == ord("k"):
            run_time -= 0.1
            print(run_time)
            print("Straight" , str(run_time + 0.5))
        elif k == ord("o"):
            if camera_mode < 3:
                camera_mode += 1
                print("camera_mode set "+ str(camera_mode) + ".")
        elif k == ord("l"):
            if camera_mode > 1:
                camera_mode -= 1
                print("camera_mode set "+ str(camera_mode) + ".")
        elif k == 27:
            break
        """
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
    """
    except KeyboardInterrupt:
        print("safe end.")
        break
cv2.destroyAllWindows()
cap.release
GPIO.cleanup()
print("All end.")
