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
        # RUN 2: ?? Points
        #########################################################

        # M08: Watch Television - 20 points
        driveStraight(35, 510, True)
        sleep(2)
        driveStraight(20, 70, True)
         # M07: Wind Turbine - 30 points
        driveStraight(-15, 125, True)
        RWheel.on_for_degrees(20, 185)
        RWheelShutdown()
        driveStraight(30, 340, True)
        '''
        lineDetect(15, 3, "Black", False)
        lineDetect(15, 3, "White", True)
        driveStraight(15, 90, True)
        LWheel.on_for_degrees(20, 345)
        LWheelShutdown()
        driveStraight(20, 250, True)
        sleep(0.5)
        driveStraight(-20, 70, True)
        driveStraight(20, 80, True)
        sleep(0.5)
        driveStraight(-20, 70, True)
        driveStraight(20, 90, True)
        sleep(0.5)
        driveStraight(-20, 60, True)
        driveStraight(20, 90, True)
        sleep(0.5)
        driveStraight(-20, 60, True)
        # sleep(2.0)
        LWheel.on_for_degrees(-20, 60)
        LWheelShutdown()
        # sleep(2.0)
        driveStraight(-30, 270, True)
        sleep(0.5)
        RWheel.on_for_degrees(20, 140)
        RWheelShutdown()
        LWheel.on_for_degrees(-20, 150)  
        LWheelShutdown()
        driveStraight(-70, 1050, True)

        # Returning to masterProgram(), resetting display.
        PrintRunNumbersToDisplay()'''

