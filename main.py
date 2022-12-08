#!/usr/bin/env python3
# 
# Filename: main.py
#

import os
import sys

from allRuns import *
from runSelected import *


def masterProgram():
    print("Starting masterProgram()", file=sys.stderr)

    # Assign each Run to each of the labeled Buttons on the EV3 Brick
    btn.on_left = Run1
    btn.on_enter = Run2
    btn.on_right = Run3
    btn.on_up = Run4
    btn.on_down = Run5
    # btn.on_down = ReassignRunButtons

    PrintRunNumbersToDisplay()

    # Loop while waiting for a Button to be pressed
    while True:
        btn.process()
        sleep(0.1)    


def main():
    # Print to the output panel in Visual Studio Code to show the program has started
    print("Starting main()", file=sys.stderr)

    sound.set_volume(pct=40)
    sound.play_file('/home/robot/sounds/download.wav', volume=40)
    
    WheelSetup()
    FrontMotorSetup()
    BackMotorSetup()

    # Always have exactly ONE of the next two lines uncommented OR ELSE the bot will do nothing.
    # runSelected()   # Uncomment this line when you only want to work on your Run without using the MasterProgram
    masterProgram()  # Uncomment this line when you want to run MasterProgram

if __name__ == '__main__':
    main()
