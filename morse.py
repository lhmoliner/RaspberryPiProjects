#!/usr/bin/python

import RPi.GPIO as GPIO
from time import sleep

led = 7
GPIO.setmode(GPIO.BOARD)
GPIO.setup(led, GPIO.OUT)
sleep_time = 0.2
long_time = .6
short_time = .2

def beep(time):
    GPIO.output(led, True)
    sleep(time)
    GPIO.output(led, False)
    sleep(sleep_time)

def long():
    beep(long_time)

def short():
    beep(short_time)
 
def pattern(*args):
   for method in args:
	method()

options = {"A" : pattern(short,long),
	"B" : lambda : pattern(long,short,short,short),
	"C" : lambda : pattern(long,short,long,short),
	"D" : lambda : pattern(long,short,short),
	"E" : lambda : pattern(short),
	"F" : lambda : pattern(short,short,long,short),
	"G" : lambda : pattern(long,long,short),
	"H" : lambda : pattern(short,short,short,short),
	"I" : lambda : pattern(short,short),
	"J" : lambda : pattern(short,long,long,long),
	"K" : lambda : pattern(long,short,long),
	"L" : lambda : pattern(short,long,short,short),
	"M" : lambda : pattern(long,long),
	"N" : lambda : pattern(long,short),
	"O" : lambda : pattern(long,long,long),
	"P" : lambda : pattern(short,long,long,short),
	"Q" : lambda : pattern(long,long,short,long),
	"R" : lambda : pattern(short,long,short),
	"S" : lambda : pattern(short,short,short),
	"T" : lambda : pattern(long),
	"U" : lambda : pattern(short,short,long),
	"V" : lambda : pattern(short,short,short,long),
	"W" : lambda : pattern(short,long,long),
	"X" : lambda : pattern(long,short,short,long),
	"Y" : lambda : pattern(long,short,long,long),
	"Z" : lambda : pattern(long,long,short,short)}
try:
    while True:
        character = raw_input("insert char\n-->")
        options[character]()
except:
    GPIO.cleanup()
