#!/usr/bin/python3
#//////////////////////////////////////
#	etchASketchGPIO.py
# etch a sketch inspired game that takes in GPIO or Keyboard inputs to move cursor, Keyboard clears (shake)
#//////////////////////////////////////
import Adafruit_BBIO.GPIO as GPIO
import smbus
import time
import curses

#setup LED Matrix
bus = smbus.SMBus(2)  # Use i2c bus 1
matrix = 0x70         # Use address 0x70

delay = 1; # Delay between images in s

bus.write_byte_data(matrix, 0x21, 0)   # Start oscillator (p10)
bus.write_byte_data(matrix, 0x81, 0)   # Disp on, blink off (p11)
bus.write_byte_data(matrix, 0xe7, 0)   # Full brightness (page 15)

#set up GPIOS
buttonLeft = "P8_7"
buttonUp = "P8_8"
buttonDown = "P8_9"
buttonRight = "P8_10"
buttonClear = "P8_15"

GPIO.setup(buttonLeft, GPIO.IN) 
GPIO.setup(buttonUp, GPIO.IN)
GPIO.setup(buttonDown, GPIO.IN)
GPIO.setup(buttonRight, GPIO.IN)
GPIO.setup(buttonClear, GPIO.IN) #GPIO setup complete

def moveCursor(button): #checks push bottons and adjusts cursor accordingly
    global xpos, ypos, matrix, sketch
    if button == buttonUp:
        if ypos < 0x80:
            ypos <<= 1 
    elif button == buttonDown:
        if ypos > 1:
            ypos >>= 1
    elif button == buttonLeft:
        if xpos > 1:
            xpos -= 2
    elif button == buttonRight:
        if xpos < 15:
            xpos += 2
    elif button == buttonClear:
        sketch = [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00
    ]
    sketch[xpos-1] += int(ypos)
    bus.write_i2c_block_data(matrix, 0, sketch)
    print(xpos,"   ",ypos)
    for fade in range(0xef, 0xe0, -1):
        bus.write_byte_data(matrix, fade, 0)
        time.sleep(0.01) #debounce delay

xpos = 1 #initiliaze cursor at top left of window
ypos = 0x80

GPIO.add_event_detect(buttonLeft, GPIO.FALLING, callback=moveCursor) #events to react to a GPIO input
GPIO.add_event_detect(buttonUp, GPIO.FALLING, callback=moveCursor)
GPIO.add_event_detect(buttonRight, GPIO.FALLING, callback=moveCursor)
GPIO.add_event_detect(buttonDown, GPIO.FALLING, callback=moveCursor)
GPIO.add_event_detect(buttonClear, GPIO.FALLING, callback=moveCursor)

# The first byte is GREEN, the second is RED.
sketch = [0x80, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00
]
bus.write_i2c_block_data(matrix, 0, sketch)
for fade in range(0xef, 0xe0, -1):
    bus.write_byte_data(matrix, fade, 0)

print("Etch-A-Sketch Start")
while True: 
    time.sleep(1000)
