#coding:utf-8

import RPi.GPIO as GPIO
import time

led = 24

GPIO.setmode(GPIO.BCM)
GPIO.setup(led, GPIO.OUT, initial=GPIO.LOW)


for i in range(10):
    GPIO.output(led, 1)
    time.sleep(1)
    GPIO.output(led, 0)
    time.sleep(1)

GPIO.cleanup()
