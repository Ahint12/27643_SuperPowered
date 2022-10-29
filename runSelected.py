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

        driveStraight(40, 1400, False)
        lineSquare(15, 'White', 'Left', 0.2)
        lineSquare(15, 'Black', 'Right', 0.2)
        LWheel.on_for_degrees(20, 360)
        LWheelShutdown()
        driveStraight(30, 120, True)
        RWheel.on_for_degrees(30, 210)
        RWheelShutdown()
        driveStraight(30, 300, True)
        LWheel.on_for_degrees(20, 170)
        LWheelShutdown()
        driveStraight(25, 120, True)
        lineSquare(15, 'Black', 'Right', 0.2)
        lineSquare(15, 'White', 'Left', 0.2)
        driveStraight(25, 170, True)
        RWheel.on_for_degrees(20, 300)
        RWheelShutdown()
        driveStraight(25, 250, True)
        RWheel.on_for_degrees(20, 230)
        RWheelShutdown()
'''     driveStraight(20, 150, True)
        RWheel.on_for_degrees(-15, 355)
        RWheelShutdown()
        # PLF_Degrees1(2, -1, 225, True)
        driveStraight(15, 200, True)
        sleep(0.5)
        driveStraight(-30, 200, True)
        RWheel.on_for_degrees(30, 310)
        RWheelShutdown()
        driveStraight(80, 1600, True)
'''
