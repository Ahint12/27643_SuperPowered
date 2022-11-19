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
        #########################################################
        # RUN 3: ?? Points
        #########################################################

        driveStraight(25, 165, True)
        RWheel.on_for_degrees(15, 210, True)
        WheelShutdown()
        driveStraight(40, 1000, False)
        lineSquare(15, 'Black', 'Right', 0.2)
        lineSquare(15, 'White', 'Left', 0.2)
        WheelShutdown()
        LWheel.on_for_degrees(15, 150, True)
        WheelShutdown()
        turnLineDetect('B',15, 3,'Black', True)
        turnLineDetect('B',15, 3,'White', True)
        sleep(2.0)
        LWheel.on_for_degrees(15, 70, True)
        WheelShutdown()
        sleep(2.0)
        driveStraight(30, 220, True)
        sleep(2.0)
        RWheel.on_for_degrees(15, 170, True)
        WheelShutdown()
        driveStraight(30, 250, True)
        move_tank(15, -15, 80, True)
        WheelShutdown()

