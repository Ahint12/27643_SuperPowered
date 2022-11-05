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


def Trun1A():
    motorStall('A', -15, -12)
    motorStall('D', 8, 5)



def runSelected():

    if (True):        
        # Start coding your Run here
        print("Starting runSelected()", file=sys.stderr)

        # M10: Power Plant - 25 points
        run1A = Thread(target=Trun1A)
        run1A.start()
        driveStraight(25, 250, True)
        LWheel.on_for_degrees(25, 180)
        WheelShutdown()
        driveStraight(50, 1000, False)
        lineSquare(15, 'Black', 'Right', 0.1)
        lineSquare(15, 'White', 'Left', 0.1)
        move_tank.on_for_degrees(20, -20, 180)
        WheelShutdown()
        move_steering.on_for_degrees(0, 30, 170)
        # lineSquare(15, 'Black', 'Left', 0.3)
        # lineSquare(-15, 'White', 'Right', 0.2)
        # lineSquare(10, 'Black', 'Left', 0.1)
        FrontMotor.on_for_degrees(95, 125)
        motorStall('A', 20, 15)
        LWheel.on_for_degrees(-15, 40)
        WheelShutdown()
        FrontMotor.on_for_degrees(-45, 95)
        sleep(0.5)
        FrontMotorShutdown()
        LWheel.on_for_degrees(15, 50)
        WheelShutdown()
        lineSquare(-15, 'White', 'Left', 0.3)
        lineSquare(15, 'Black', 'Right', 0.2)
        lineSquare(-15, 'White', 'Left', 0.15)
        driveStraight(-40, 870, True)
        motorStall('D', -15, -12)
        driveStraight(15, 80, True)
        motorStall('D', 20, 16)
        driveStraight(50, 400, True)
        RWheel.on_for_degrees(30, 260)
        driveStraight(80, 1700, True)


