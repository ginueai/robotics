import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(12,GPIO.OUT)

try:
  while 1:
    GPIO.output(12,1)
    time.sleep(1)
    GPIO.output(12,0)
    time.sleep(1)
 
finally:
  GPIO.cleanup()

