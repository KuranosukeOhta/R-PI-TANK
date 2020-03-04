# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 16:00:05 2020

@author: LEGOnosuke
"""
print("WAIT PLEASE...")
gpio_pin = 17
gpio_pin2 = 27
#1= left
#2= right
import Adafruit_PCA9685
import sys
import time
import cv2
import numpy as  np
import RPi.GPIO as GPIO
cap = cv2.VideoCapture(0)
cap2 = cv2.VideoCapture(1)
change = 10

#PCA9685 settings
pwm = Adafruit_PCA9685.PCA9685()
pwm.set_pwm_freq(50)
stop = 0.5
set1 = 370
set2 = 330
pwm.set_pwm(0, 0, set1)
pwm.set_pwm(1, 0, set2)


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
camera_mode = 2
print("SETUP OK")
print("---------------CONTROLS----------------------")
a = 0.1
time.sleep(a)
print("W:go straight A,D:trun right or left")
time.sleep(a)
print("Y,G,H,J : 180*Camera control")
time.sleep(a)
print("I,K : move control")
time.sleep(a)
print("O,L : camera mode set")
time.sleep(a)
print("esc : exit program")
time.sleep(a)
print("---------------------------------------------")
print("camera screen booting...")
while True:


    try:
        ret,frame2 = cap2.read()
        cv2.imshow("180* Camera",frame2)
        ret, frame = cap.read()
        if camera_mode == 2:
            cv2.imshow("Front Camera", frame)
        else:
            gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
            if camera_mode == 1:
                if before is None:
                    before = gray.copy().astype("float")
                    continue
                cv2.imshow("Front Camera", gray)

            else:

                #before = gray.copy().astype("float")

                #ret,two = cv2.threshold(gray,147,255,cv2.THRESH_BINARY)
                ret,two = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)
                cv2.imshow("Front Camera", two)
                """
                cv2.accumulateWeighted(gray, before, 0.7)
                mdframe = cv2.absdiff(gray, cv2.convertScaleAbs(before))


                ret,thresh2 = cv2.threshold(mdframe,10,255,cv2.THRESH_BINARY)

                ret,thresh1 = cv2.threshold(gray,147,255,cv2.THRESH_BINARY)
                cv2.imshow("threshed1", thresh1)
                """





        k = cv2.waitKey(1)&0xff
        #DC
        if k == ord("w"):
            print("Straight")
            Straight(0)
        elif k == ord("a"):
            print("Left")
            Right(0)
        elif k == ord("d"):
            print("Right")
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

        #PCA9685
        elif k == ord("y"):
            set1 -= change
        elif k == ord("h"):
            set1 += change
        elif k == ord("g"):
            set2 += change
        elif k == ord("j"):
            set2 -= change

        pwm.set_pwm(0, 0, set1)
        pwm.set_pwm(1, 0, set2)
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
        print("SAFE END.")
        break
cv2.destroyAllWindows()
cap.release
GPIO.cleanup()
print("All END.")
