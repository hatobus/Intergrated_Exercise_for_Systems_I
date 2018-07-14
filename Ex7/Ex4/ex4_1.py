import RPi.GPIO as GPIO
import time

servo = 24

GPIO.setmode(GPIO.BCM)
GPIO.setup(servo, GPIO.OUT, initial=GPIO.LOW)

p = GPIO.PWM(servo, 50)

p.start(0)

dutycycle = [2.5, 5.0, 7.5, 9.75, 12]

p.ChangeDutyCycle(7.5)
time.sleep(1)

try:
    while True:
        for c in dutycycle:
            p.ChangeDutyCycle(c)
            time.sleep(1)

except KeyboardInterrupt:
    p.stop()
    GPIO.cleanup()
