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

        driveStraight(25, 340, True)
        FrontMotor.on_for_degrees(-60, 60, True)
        FrontMotor.on_for_degrees(60, 100, True)
        sleep(0.5)
        motorStall('A', -30, -20)
        driveStraight(-20, 120, True)
        LWheel.on_for_degrees(15, 185, True)
        WheelShutdown()

