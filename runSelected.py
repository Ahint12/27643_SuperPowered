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
    motorStall('A', 15, 12)
    motorStall('D', 7, 5)

def Trun6B():
    motorStall('A', -10, -7)
    
def runSelected():

    if (True):        
        # Start coding your Run here
        print("Starting runSelected()", file=sys.stderr)



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
