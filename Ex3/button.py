import RPi.GPIO as GPIO
import time


button = 25
led = 24

GPIO.setmode(GPIO.BCM)
GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


print("push button")

while True:
    btn = GPIO.input(button)
    if btn == True:
        print("pushed")
        break

    time.sleep(1)

GPIO.cleanup()
