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
from flask import Flask, render_template, request
app = Flask(__name__)

#setup LED Matrix
bus = smbus.SMBus(2)  # Use i2c bus 1
matrix = 0x70         # Use address 0x70

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

@app.route("/")
def index():
	return render_template('index.html')
	
@app.route("/<action>")
def action(action):
    global xpos
    global ypos
    global sketch
    global matrix
    if action == "up":
        if ypos < 0x80:
            ypos <<= 1 
    elif action == "down":
        if ypos > 1:
            ypos >>= 1
    elif action == "left":
        if xpos > 1:
            xpos -= 2
    elif action  == "right":
        if xpos < 15:
            xpos += 2
    elif action  == "clear":
        sketch = [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00
    ]
    sketch[xpos-1] |= int(ypos)
    bus.write_i2c_block_data(matrix, 0, sketch)
    time.sleep(0.01) #debounce delay
    return render_template('index.html')
    
if __name__ == "__main__":
   app.run(host='0.0.0.0', port=8081, debug=True)
   