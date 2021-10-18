#!/usr/bin/env python3
# From: https://towardsdatascience.com/python-webserver-with-flask-and-raspberry-pi-398423cc6f5d
#	flaskEtchASketchGPIO.py
# etch a sketch inspired game that takes in inputs from flask
'''
	Etch A Sketch
'''
import smbus
import time
import curses
import Adafruit_BBIO.GPIO as GPIO

#setup LED Matrix
bus = smbus.SMBus(1)  # Use i2c bus 1 
matrix = 0x70         # Use address 0x70
#setup the accelerometer
accelerometer = 0x53
axes_data = 0x32
bus.write_byte_data(accelerometer, 0x2C, 0x0B) #set Baud rate
bus.write_byte_data(accelerometer, 0x2D, 0x08) #enable Measurment
 
        
 

delay = 1; # Delay between images in s

bus.write_byte_data(matrix, 0x21, 0)   # Start oscillator (p10)
bus.write_byte_data(matrix, 0x81, 0)   # Disp on, blink off (p11)
bus.write_byte_data(matrix, 0xe7, 0)   # Full brightness (page 15)

xpos = 1 #initiliaze cursor at top left of window
ypos = 0x80

# The first byte is GREEN, the second is RED.
sketch = [0x80, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]
bus.write_i2c_block_data(matrix, 0, sketch)

print("Etch-A-Sketch Start")

action = "up"

while 1 :
    accelData = bus.read_i2c_block_data(accelerometer, axes_data ,6)
    accelX = accelData[0]-accelData[1]
    accelY = accelData[2]-accelData[3]
    accelZ = accelData[4]-accelData[5]
    print('X')
    print(accelX)
    print()
    print('Y')
    print(accelY)
    print()
    print('Z')
    print(accelZ)
    print()
    if accelY < -200:
        if ypos < 0x80:
            ypos <<= 1 
    if accelY > 200:
        if ypos > 1:
            ypos >>= 1
    if accelX > 200:
        if xpos > 1:
            xpos -= 2
    if accelX < -200:
        if xpos < 15:
            xpos += 2
    if accelZ < 0:
        sketch = [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]
    sketch[xpos-1] |= int(ypos)
    bus.write_i2c_block_data(matrix, 0, sketch)
    time.sleep(1) #debounce delay
