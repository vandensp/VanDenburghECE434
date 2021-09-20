switchesAndLights.py
  sets pushbuttons to inputs in GPIO ports and corresponding LED outputs that light up when their respective buttons are pressed.

etchASketchGPIO.py
  plays an etch a sketch game that can be controlled by either the keyboard or pushbuttons. both can move the cursor or clear the screen. The game can be exited using "x" on the keyboard.

GPIO Questions/Answers Below

Measuring a gpio pin on an Oscilloscope
1.	What's the min and max voltage?
	Min = -110 mv
	Max = 3.39V
2.	What period and frequency is it?
	Period = 242.49 ms
	Frequency = 4.123 Hz
3.	How close is it to 100ms?
	142.49 ms
4.	Why do they differ?
	Other processies on the chip interrupt the program controlling the GPIO cycling.
5.	Run htop and see how much processor you are using.
	1.3%
6.	Try different values for the sleep time (2nd argument). What's the shortest period you can get?
	| Sleep Value      |  Period  | Processor Power |
	| :--------------: | :------: | :-------------: |
	| 0.2              | 439.0 ms | 0.7%            |
	| 0.1              | 242.49 ms| 1.3%            |
	| 0.09             | 220.0 ms | 1.3%            |
	| 0.005            | 50.0 ms  | 12.8%           |
	| 0                | 41.5 ms  | 18.8%           |
	| 0(after cleanup) | 14.55 ms | 21.3%           |
7.	How stable is the period?
        The period wavers by approximately 1 ms with occasional spikes.
8.	Try launching something like vi. How stable is the period?
	Significantly less. The spikes, there are 20-30 ms spikes approximately every second.
9.	Try cleaning up togglegpio.sh and removing unneeded lines. Does it impact the period?
	Greatly, the period dropped to 14.5 ms.
10.	togglegpio uses bash (first line in file). Try using sh. Is the period shorter?
	Yes, the period dropped to under 1 ms for a short period of time before rising up.
11.	What's the shortest period you can get?
	285 microseconds for a very short moment. The shortest stable time is 11 ms.

Python 
Write a python script to toggle a gpio pin as fast as possible.  
1.	What period and frequency is it?
	Period = 166.5 us
	Frequency = 6.01 kHz
2.	Run htop and see how much processor you are using.
	94.3%
3.	Present the shell script and Python script results in a table for easy comparison. 
	(Table inserted below)
C
Repeat the above using C.  Modify togglegpio.c to use lseek() instead of opening and cloning the file.  How much faster is it?  Add your results to the table

gpiod
gpiod is the new gpio pins that replaces /sys/class/gpio.  There are several gpiod examples in /var/lib/cloud9.
Use the toggle1 examples measure how fast you can toggle one gpio bit use c and python.  Repeat the exercise using two bits.  Add the results to your table.

|               | Shell Script | Python   |   C      | Python (gpiod 1 bit) | C (gpiod 1 bit) | Python (gpiod 2 bit) | C (gpiod 2 bit) |
| :-----------: | :----------: | :------: | :------: | :------------------: | :-------------: | :------------------: | :-------------: |
| Max Frequency | 68.7 Hz      | 6.01 kHz | 7.63 kHz | 56.2 kHz             | 294 kHz         | 54.1 kHz             | 271 kHz         |
| Min Period    | 14.55 ms     | 166.5 us | 131 us   | 17.8 us              | 3.4 us          | 18.5 us              | 3.69 us         |
