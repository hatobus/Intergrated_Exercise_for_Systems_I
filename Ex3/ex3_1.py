import RPi.GPIO as GPIO
import time


button = 25
led = 24

# Setting the GPIO state
GPIO.setmode(GPIO.BCM)
GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(led, GPIO.OUT, initial=GPIO.LOW)

print("push button")

while True:

    # Lokking button pin state
    btn = GPIO.input(button)
    
    if btn:
        print("Blink 7 sec")
        GPIO.output(led, 1)
        time.sleep(7)
        break

    time.sleep(1)

GPIO.cleanup()
