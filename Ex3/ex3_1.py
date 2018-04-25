import RPi.GPIO as GPIO
import time


button = 25
led = 24

GPIO.setmode(GPIO.BCM)
GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(led, GPIO.OUT, initial=GPIO.LOW)

print("push button")

while True:
    btn = GPIO.input(button)
    if btn:
        print("Blink 7 sec")
        
        for i in range(7):
            GPIO.output(led, 1)
            time.sleep(0.5)
            GPIO.output(led, 0)
            time.sleep(0.5)

        break

    time.sleep(1)

GPIO.cleanup()
