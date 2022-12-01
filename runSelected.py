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


def Trun6A():
    motorStall('A', -15, -7)
    motorStall('D', -10, -7)
    BackMotor.on_for_degrees(10, 60)
    BackMotorShutdown()

    
def runSelected():

    if (True):        
        # Start coding your Run here
        print("Starting runSelected()", file=sys.stderr)

        run4A = Thread(target=Trun6A)
        run4A.start()
        move_steering.on_for_degrees(0, 30, 180)    
        turnLineDetect('B', 25, 2, 'Black', True)
        turnLineDetect('C', 15, 2, 'Black', False)
        turnLineDetect('C', 15, 2, 'White', True)
        PLF_Degrees1(2, -1, 500, False)
        PLF_LineDetect1(2, -1, True)
        RWheel.on_for_degrees(20, 340)
        RWheelShutdown()
        FrontMotor.on_for_degrees(30, 100)
        FrontMotor.on_for_degrees(-30, 100)
        FrontMotor.on_for_degrees(30, 100)
        FrontMotor.on_for_degrees(-30, 100)
        FrontMotor.on_for_degrees(30, 100)
        FrontMotor.on_for_degrees(-30, 100)
        FrontMotorShutdown()
        #####
        # M03: Energy Storage - Put 3 Energy Units Into the Energy Storage Bin, Remove Energy Storage Tray - 30 points 10 x 3 energy units
        # 5 points for removing tray from Energy Storage model.
        #####
        lineSquare(-15, "Black", "Left", 0.2)
        lineSquare(-15, "White", "Left", 0.1)
        driveStraight(-20, 20, True)
        RWheel.on_for_degrees(20, 180)
        RWheelShutdown()
        driveStraight(25, 45, True)
        RWheel.on_for_degrees(20, 195)
        RWheelShutdown()
        driveStraight(-20, 80, True)
        BackMotor.on_for_degrees(-20, 37)
        BackMotorShutdown()
        move_steering.on_for_degrees(12, 80, 2000)
        WheelShutdown()


        '''
        oneWheelTurn('Left', 170, 3500, 83)
        sleep(1.0)
        oneWheelTurn('Left', 170, 3500, -83)
        sleep(1.0)
        oneWheelTurn('Right', 170, 3500, 83)
        sleep(1.0)
        oneWheelTurn('Right', 170, 3500, -83)
        sleep(1.0)
        twoWheelTurn('Left', 170, 3500, 165)
        sleep(1.0)
        twoWheelTurn('Left', 170, 3500, -165)
        sleep(1.0)
        twoWheelTurn('Right', 170, 3500, 165)
        sleep(1.0)
        twoWheelTurn('Right', 170, 3500, -165)
        sleep(1.0)
        '''
