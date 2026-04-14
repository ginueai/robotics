import RPi.GPIO as GPIO
import time

pin_no = 21
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin_no,GPIO.OUT)

try:
  while 1:
    GPIO.output(pin_no,1)
    time.sleep(5)
    GPIO.output(pin_no,0)
    time.sleep(1)
 
finally:
  GPIO.cleanup()
