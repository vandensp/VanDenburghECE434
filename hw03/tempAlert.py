#!/usr/bin/env python3

import smbus
import time
import Adafruit_BBIO.GPIO as GPIO

bus = smbus.SMBus(2)
address1 = 0x48
address2 = 0x4A

temp1alert= "P8_17"
temp2alert = "P8_18"

bus.write_byte_data(address1, 2, 20) #set high and low temps (27C/80.6F - 28C/82.4F)
bus.write_byte_data(address1, 3, 28)
bus.write_byte_data(address2, 2, 20)
bus.write_byte_data(address2, 3, 28)

def detect(alert):
    print(alert,": Temperatrue Alert!")
    time.sleep(5)

GPIO.setup(temp1alert, GPIO.IN)
GPIO.setup(temp2alert, GPIO.IN)

GPIO.add_event_detect(temp1alert, GPIO.BOTH, callback=detect)
GPIO.add_event_detect(temp2alert, GPIO.BOTH, callback=detect)

while True:
    temp1 = bus.read_byte_data(address1, 0) #*(9/5)) + 32
    temp2 = bus.read_byte_data(address2, 0) #*(9/5)) + 32
    print("temp1 = ",temp1," temp2 = ",temp2,end="\r")
    time.sleep(0.25)
