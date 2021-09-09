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

xpos = 0 #initiliaze cursor at top left of window
ypos = 0

#Welcome message
window.addstr(ypos, xpos, "Welcome to Etch-A-Sketch! \n" +
                           "Move using the arror keys, \n" +
                           "Clear the window with 'c'\n" +
                           "Exit with 'x' \n\n" +
                           "Press any button to start now!", curses.A_BOLD)
window.refresh()

key = window.getch() #after any button press, begins with cursor at top left
window.clear()
window.addch(ypos, xpos, '*', curses.A_BOLD)

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