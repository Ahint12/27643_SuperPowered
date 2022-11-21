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

        # run5A = Thread(target=Trun5A)
        # run5A.start()
        driveStraight(25, 400, True)
        motorStall('A', -20, -15)
        driveStraight(-25, 120, True)
        LWheel.on_for_degrees(15, 175, True)
        WheelShutdown()

