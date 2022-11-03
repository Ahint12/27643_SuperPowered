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

        # M10: Power Plant - 25 points
        motorStall('A', 20, 10)
        motorStall('D', 10, 8)
        FrontMotorShutdown()
        driveStraight(50, 1300, False)
        lineSquare(15, 'Black', 'Right', 0.1)
        lineSquare(15, 'White', 'Left', 0.1)
        motorStall('A', -40, -30)
        move_tank.on_for_degrees(20, -20, 185)
        WheelShutdown()
        sleep(2.0)
        lineSquare(15, 'Black', 'Right', 0.2)
        sleep(2.0)
        FrontMotor.on_for_degrees(95, 125)
        motorStall('A', 20, 10)
        FrontMotorShutdown()
        LWheel.on_for_degrees(-15, 50)
        WheelShutdown()
        FrontMotor.on_for_degrees(-20, 100)
        FrontMotorShutdown()
        lineSquare(15, 'Black', 'Left', 0.3)
        lineSquare(15, 'White', 'Right', 0.2)
        lineSquare(-15, 'Black', 'Left', 0.15)
        driveStraight(-40, 900, True)
        motorStall('D', -10, -8)
        driveStraight(15, 80, True)
        motorStall('D', 10, 8)
        driveStraight(50, 400, True)
        RWheel.on_for_degrees(30, 260)
        driveStraight(80, 1700, True)



