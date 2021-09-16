#!/usr/bin/python3
#//////////////////////////////////////
#	switchesAndLights.py
#	uses GPIOs to have pushbuttons light up LEDs
#   Author: Samuel VanDenburgh
#   Date: 16 September 2021
#//////////////////////////////////////
import Adafruit_BBIO.GPIO as GPIO
import time

def blink(button):
    state = GPIO.input(button)
    GPIO.output(map[button], state)

button1 = "P8_7"
button2 = "P8_8"
button3 = "P8_9"
button4 = "P8_10"

LED1 = "P8_14"
LED2 = "P8_13"
LED3 = "P8_12"
LED4 = "P8_11"

GPIO.setup(button1, GPIO.IN)
GPIO.setup(button2, GPIO.IN)
GPIO.setup(button3, GPIO.IN)
GPIO.setup(button4, GPIO.IN)
 
GPIO.setup(LED1, GPIO.OUT)
GPIO.setup(LED2, GPIO.OUT)
GPIO.setup(LED3, GPIO.OUT)
GPIO.setup(LED4, GPIO.OUT)

map = {button1: LED1, button2: LED2, button3: LED3, button4: LED4}

GPIO.add_event_detect(button1, GPIO.BOTH, callback=blink)
GPIO.add_event_detect(button2, GPIO.BOTH, callback=blink)
GPIO.add_event_detect(button3, GPIO.BOTH, callback=blink)
GPIO.add_event_detect(button4, GPIO.BOTH, callback=blink)
 
while True:
    time.sleep(1000)