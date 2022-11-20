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


def Trun4A():
    motorStall('A', -15, -7)
    motorStall('D', -10, -7)
    BackMotor.on_for_degrees(10, 60)
    BackMotorShutdown()


def runSelected():

    if (True):        
        # Start coding your Run here
        print("Starting runSelected()", file=sys.stderr)
        #########################################################
        # RUN 3: ?? Points
        #########################################################

        driveStraight(25, 170, True)
        WheelShutdown()
        RWheel.on_for_degrees(15, 170, True)
        # RWheel.on_for_degrees(15, 180, True)   # ASHBOT
        WheelShutdown()
        driveStraight(40, 1000, False)
        lineSquare(15, 'Black', 'Right', 0.2)
        lineSquare(15, 'White', 'Left', 0.2)
        WheelShutdown()
        LWheel.on_for_degrees(15, 150, True)
        WheelShutdown()
        turnLineDetect('B',15, 3,'Black', True)
        turnLineDetect('B',15, 3,'White', True)
        LWheel.on_for_degrees(15, 70, True)
        WheelShutdown()
        driveStraight(30, 170, True)
        RWheel.on_for_degrees(15, 170, True)
        WheelShutdown()
        driveStraight(30, 280, True)
        move_tank.on_for_degrees(15, -15, 70, True)
        WheelShutdown()
        driveStraight(30, 150, True)
        lineSquare(20, 'Black', 'Right', 0.2)
        lineSquare(20, 'White', 'Left', 0.2)
        RWheel.on_for_degrees(15, 60, True)
        WheelShutdown()
        driveStraight(30, 260, True)
        RWheel.on_for_degrees(15, 250, True)
        WheelShutdown()
        driveStraight(30, 220, True)
        RWheel.on_for_degrees(15, 260, True)
        driveStraight(30, 100, True)
        lineSquare(20, 'White', 'Right', 0.2)
        lineSquare(20, 'Black', 'Left', 0.2)
