#!/usr/bin/python3
#//////////////////////////////////////
#	etchASketch.py
# etch a sketch inspired game that takes in keyboard inputs to move cursor and clear(shake).
#//////////////////////////////////////

import time
import curses

window = curses.initscr() #initialize and set up curses
curses.noecho()
curses.cbreak()
window.keypad(True)
curses.curs_set(False)

xpos = 0
ypos = 0

print("etchASketch start...\n")


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
curses.echo()
curses.endwin()