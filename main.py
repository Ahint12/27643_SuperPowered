#!/usr/bin/env python3
# 
# Filename: main.py
#

import os
import sys
# import config

from allRuns import *
from runSelected import *

def masterProgram():
    print("Starting masterProgram()", file=sys.stderr)

    # Assign each Run to each of the labeled Buttons on the EV3 Brick
    btn.on_left = run1
    btn.on_enter = run2
    btn.on_right = run3
    btn.on_up = run4
    btn.on_down = run5
    # btn.on_down = ReassignRunButtons


    # Loop while waiting for a Button to be pressed
    while True:
        btn.process()
        sleep(0.1)    


def main():
    # Print to the output panel in Visual Studio Code to show the program has started
    print("Starting main()", file=sys.stderr)

    sound.set_volume(pct=40)
    sound.play_file('/home/robot/sounds/download.wav', volume=40)
    # sound.play_file('/home/robot/sounds/NeverGonnaGive.wav', volume=40)
    
    WheelSetup()
    FrontMotorSetup()
    BackMotorSetup()

    # Always have exactly ONE of the next two lines uncommented OR ELSE the bot will do nothing.
    # runSelected()   # Uncomment this line when you only want to work on your Run without using the MasterProgram
    masterProgram()  # Uncomment this line when you want to run MasterProgram


if __name__ == '__main__':
    main()
