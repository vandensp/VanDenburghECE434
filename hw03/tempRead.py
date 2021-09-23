#!/usr/bin/env python3
#Read two TMP101 sensors

import smbus
import time

bus = smbus.SMBus(2)
address1 = 0x48
address2 = 0x4A

while True:
    temp1 = (bus.read_byte_data(address1, 0)*(9/5)) + 32
    temp2 = (bus.read_byte_data(address2, 0)*(9/5)) + 32
    print("temp1 = ",temp1," temp2 = ",temp2,end="\r")
    time.sleep(0.25)