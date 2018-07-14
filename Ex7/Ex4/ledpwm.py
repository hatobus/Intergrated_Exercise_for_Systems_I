#coding:utf-8

import RPi.GPIO as GPIO
import time

led = 24

GPIO.setmode(GPIO.BCM)
GPIO.setup(led, GPIO.OUT, initial=GPIO.LOW)

p = GPIO.PWM(led, 1000)

p.start(0)

for i in range(3):
    for dutyratio in range(0, 101, 10):
        p.ChangeDutyCycle(dutyratio)
        time.sleep(1)
    for dutyratio in range(100, -1, -10):
        p.ChangeDutyCycle(dutyratio)
        time.sleep(1)

p.stop()
GPIO.cleanup()
