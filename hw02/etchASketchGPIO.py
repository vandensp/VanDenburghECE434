#!/usr/bin/python3
#//////////////////////////////////////
#	etchASketchGPIO.py
# etch a sketch inspired game that takes in GPIO or Keyboard inputs to move cursor, Keyboard clears (shake)
#//////////////////////////////////////
import Adafruit_BBIO.GPIO as GPIO
import time
import curses

#set up GPIOS
buttonLeft = "P8_7"
buttonUp = "P8_8"
buttonDown = "P8_9"
buttonRight = "P8_10"

GPIO.setup(buttonLeft, GPIO.IN)
GPIO.setup(buttonUp, GPIO.IN)
GPIO.setup(buttonDown, GPIO.IN)
GPIO.setup(buttonRight, GPIO.IN)

def blinkAndMove(button):
    global xpos, ypos, window
    if button == buttonUp:
        if ypos > 0:
            ypos -= 1
    elif button == buttonDown:
        if ypos < (curses.LINES - 1):
            ypos += 1
    elif button == buttonLeft:
        if xpos > 0:
            xpos -= 1
    elif button == buttonRight:
        if xpos < (curses.COLS - 2):
            xpos += 1
    window.addch(ypos, xpos, '*', curses.A_BOLD)
    window.refresh()
    time.sleep(0.01) #debounce delay

window = curses.initscr() #initialize and set up curses
curses.noecho()
curses.cbreak()
window.keypad(True)
curses.curs_set(False)

xpos = 0 #initiliaze cursor at top left of window
ypos = 0

#Welcome message
window.addstr(ypos, xpos, "Welcome to Etch-A-Sketch! \n" +
                           "Move using the arror keys, \n" +
                           "Clear the window with 'c'\n" +
                           "Exit with 'x' \n\n" +
                           "Press any key on the keybaord to start now!", curses.A_BOLD)
window.refresh()

key = window.getch() #after any button press, begins with cursor at top left
window.clear()
window.addch(ypos, xpos, '*', curses.A_BOLD)

GPIO.add_event_detect(buttonLeft, GPIO.FALLING, callback=blinkAndMove)
GPIO.add_event_detect(buttonUp, GPIO.FALLING, callback=blinkAndMove)
GPIO.add_event_detect(buttonRight, GPIO.FALLING, callback=blinkAndMove)
GPIO.add_event_detect(buttonDown, GPIO.FALLING, callback=blinkAndMove)


while True: #waits for an input reacts accordingly
    key = window.getch()
    if key == curses.KEY_UP:
        if ypos > 0:
            ypos -= 1
    elif key == curses.KEY_DOWN:
        if ypos < (curses.LINES - 1):
            ypos += 1
    elif key == curses.KEY_LEFT:
        if xpos > 0:
            xpos -= 1
    elif key == curses.KEY_RIGHT:
        if xpos < (curses.COLS - 2):
            xpos += 1
    elif key == ord('c'):
        window.clear()
    elif key == ord('x'): 
        break
    window.addch(ypos, xpos, '*', curses.A_BOLD)
    window.refresh()
    
curses.nocbreak() #terminates curses and returns terminal to original mode
window.keypad(False)
window.clear()
curses.echo()
curses.endwin()