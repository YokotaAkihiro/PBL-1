import RPi.GPIO as GPIO
import time

# setup

pin = 21

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin,GPIO.OUT,initial=GPIO.LOW)
print(1)

p = GPIO.PWM(pin,1)
p.start(50)
p.ChangeFrequency(220)
time.sleep(3)
p.stop()

print(3)
GPIO.cleanup()