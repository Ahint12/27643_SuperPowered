#!/usr/bin/env python3
# 
# Filename: runSelected.py
#

import os
# from re import A
import sys
# import config

from time import sleep, time
from defineRobot import *
from myBlocks import *


def runSelected():

    if (True):        
        # Start coding your Run here
        print("Starting runSelected()", file=sys.stderr)

    # Run 2

    driveStraight(40, 760)
    driveStraight(20, 70)
    WheelShutdown()
    driveStraight(-15, 125)
    WheelShutdown()
    RWheel.on_for_degrees(20, 170)
    RWheelShutdown()
    driveStraight(30, 340)
    WheelShutdown()
    lineDetect(15, 3, "Black", False)
    lineDetect(15, 3, "White", True)
    driveStraight(15, 90)
    WheelShutdown()
    LWheel.on_for_degrees(20, 325)
    LWheelShutdown()
    driveStraight(20, 220)
    WheelShutdown()
    sleep(0.5)
    driveStraight(-20, 50)
    WheelShutdown()
    driveStraight(20, 50)
    WheelShutdown()
    sleep(0.5)
    driveStraight(-20, 50)
    WheelShutdown()
    driveStraight(20, 50)
    WheelShutdown()
    sleep(0.5)
    driveStraight(-30, 50)
    WheelShutdown()
