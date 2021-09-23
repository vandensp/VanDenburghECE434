#!/usr/bin/env python3

import smbus
import time
import Adafruit_BBIO.GPIO as GPIO

bus = smbus.SMBus(2)
address1 = 0x48
address2 = 0x4A

temp1alert= "P8_46"
temp2alert = "P8_45"

bus.write_byte_data(address1, 1, 1)
bus.write_byte_data(address2, 1, 1)

def detect(alert):
    print(alert,": Temperature is too high")
    time.sleep(0.25)

GPIO.setup(temp1alert, GPIO.IN)
GPIO.setup(temp2alert, GPIO.IN)

GPIO.add_event_detect(temp1alert, GPIO.RISING, callback=detect)
GPIO.add_event_detect(temp2alert, GPIO.RISING, callback=detect)

while True:
    time.sleep(100)