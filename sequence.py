#!/usr/bin/python

import RPi.GPIO as GPIO
import time
from random import randint

GPIO.setmode(GPIO.BOARD)
time_blink = 0.05
time_stop = 0.05
ran = randint(1,5)

def pattern(num):
	GPIO.setup(num, GPIO.OUT)
	GPIO.output(num, True)
	time.sleep(time_blink)
	GPIO.output(num, False)
	time.sleep(time_stop)

options = {1 : lambda : pattern(7),
	2 : lambda : pattern(11),
	3 : lambda : pattern(13),
	4 : lambda : pattern(15),
	5 : lambda : pattern(16)}

try:
  while True:
    options[randint(1,5)]()	
except:
  GPIO.cleanup()
