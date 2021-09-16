#!/usr/bin/python3
#//////////////////////////////////////
#	gpiotoggle.py
#	Blinks an LED as fast as possible
#   Author: Samuel VanDenburgh
#   Date: 16 September 2021
#//////////////////////////////////////
import Adafruit_BBIO.GPIO as GPIO

out = "GPIO1_28"
 
GPIO.setup(out, GPIO.OUT)
 
while True:
    GPIO.output(out, GPIO.HIGH)
    GPIO.output(out, GPIO.LOW)