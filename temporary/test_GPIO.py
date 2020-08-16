#!/usr/bin/python
# Script for Raspberry Pi Internet Radio

# import
import RPi.GPIO as GPIO
import time
import os

PRESSTIME = 0
PLAYING = False

# Define GPIO for Radio Controls
# Button 1 goes to the Pi-Supply to turn the computer on

PLAYBUTTON = 26  # Button 3 - Play. Green Wires
STOPOFF = 16  # Button 4 - Brown wires. Press for stop. Long press for shutdown.
GPIO.setmode(GPIO.BCM)  # Use BCM GPIO numbers
GPIO.setup(PLAYBUTTON, GPIO.IN)  # Play
GPIO.setup(STOPOFF, GPIO.IN)  # Short Press is stop, long press is shutdown

# Timing constants
E_PULSE = 0.00005
E_DELAY = 0.00005

def main():
    # Main program block

    # Initialise display

    # Send some test

    time.sleep(2)
    while 1:

        if (GPIO.input(PLAYBUTTON) == False):
            print("Play button pressed")

        if (GPIO.input(STOPOFF) == False):
            print("Stop button pressed")

            PRESSTIME = 0
            for j in range(50):  # start counting
                if (GPIO.input(STOPOFF) == False):  # if it is still being pressed

                    PRESSTIME = PRESSTIME + 1  # add something to J
                if (PRESSTIME >= 25):  # if you have been pressing for 28*0.1=2.8 seconds then
                    print("Stop button long pressed")

                    print
                    "the shutdown command has been sent"

                time.sleep(0.1)  # wait 0.1sec, then loop again to see if you are holding the PLAYBUTTON still




if __name__ == '__main__':
    main()
# End of File
