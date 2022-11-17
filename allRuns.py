#!/usr/bin/env python3
# 
# Filename: allRuns.py
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

def run1(state):
    if state:
        print("run1() button pressed", file=sys.stderr)  
        sound.beep()
        # Clear the first 2 rows of text on the LCD screen using the lcd.rectangle function
        lcd.rectangle(False, x1=0, y1=0, x2=177, y2=39, fill_color='white',outline_color='white')
        lcd.text_pixels("RUN 1", clear_screen=False, x=0, y=0, text_color='black', font=DisplayFont)
        lcd.update()
        print("Starting run1()", file=sys.stderr)

        #########################################################
        # RUN 1: 45 Points
        #########################################################

        # M10: Power Plant - 25 points
        run1A = Thread(target=Trun1A)
        run1A.start()
        driveStraight(25, 250, True)
        LWheel.on_for_degrees(15, 170, True)
        WheelShutdown()
        driveStraight(40, 1000, False)
        lineSquare(15, 'Black', 'Right', 0.2)
        lineSquare(15, 'White', 'Left', 0.2)
        WheelShutdown()
        move_tank.on_for_degrees(15, -15, 180, True)
        WheelShutdown()
        lineSquare(15, 'Black', 'Left', 0.15)
        driveStraight(30, 30, True)
        WheelShutdown()
        FrontMotor.on_for_degrees(95, 125)
        motorStall('A', 20, 15)
        driveStraight(-10, 15, True)
        LWheel.on_for_degrees(-15, 45, True)
        WheelShutdown()
        FrontMotor.on_for_degrees(-35, 100)
        FrontMotorShutdown()
        sleep(0.75)
        #####
        # M05: Smart Grid - 20 points (30 points if other team raises their hand)
        #####
        LWheel.on_for_degrees(15, 45, True)
        WheelShutdown()
        driveStraight(20, 20, True)
        lineSquare(-15, 'White', 'Left', 0.3)
        lineSquare(15, 'Black', 'Right', 0.2)
        lineSquare(-15, 'White', 'Left', 0.1)
        driveStraight(-40, 870, True)
        motorStall('D', -20, -17)
        driveStraight(15, 80, True)
        BackMotor.on_for_degrees(30, 50)
        BackMotorShutdown()
        driveStraight(60, 400, True)
        RWheel.on_for_degrees(30, 260, True)
        driveStraight(80, 1800, True)
        WheelShutdown()

        # Returning to masterProgram(), resetting display.
        PrintRunNumbersToDisplay()


def run2(state):
    if state:
        print("run2() button pressed", file=sys.stderr)  
        sound.beep()
        # Clear the first 2 rows of text on the LCD screen using the lcd.rectangle function
        lcd.rectangle(False, x1=0, y1=0, x2=177, y2=39, fill_color='white',outline_color='white')
        lcd.text_pixels("RUN 2", clear_screen=False, x=0, y=0, text_color='black', font=DisplayFont)
        lcd.update()
        print("Starting run2()", file=sys.stderr)
        
        #########################################################
        # RUN 2: ?? Points
        #########################################################

        # M08: Watch Television - 20 points
        driveStraight(35, 510, True)
        driveStraight(20, 70, True)
         # M07: Wind Turbine - 30 points
        driveStraight(-15, 130, True)
        RWheel.on_for_degrees(15, 175)
        RWheelShutdown()
        driveStraight(30, 400, False)
        lineDetect(15, 3, "Black", False)
        lineDetect(15, 3, "White", True)
        LWheel.on_for_degrees(20, 360)
        LWheelShutdown()
        driveStraight(20, 200, True)
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
        driveStraight(-30, 270, True)
        RWheel.on_for_degrees(20, 140)
        RWheelShutdown()
        LWheel.on_for_degrees(-20, 150)  
        LWheelShutdown()
        driveStraight(-70, 1050, True)

        # Returning to masterProgram(), resetting display.
        PrintRunNumbersToDisplay()



def run3(state):
    if state:
        print("run3() button pressed", file=sys.stderr)  
        sound.beep()
        # Clear the first 2 rows of text on the LCD screen using the lcd.rectangle function
        lcd.rectangle(False, x1=0, y1=0, x2=177, y2=39, fill_color='white',outline_color='white')
        lcd.text_pixels("RUN 3", clear_screen=False, x=0, y=0, text_color='black', font=DisplayFont)
        lcd.update()
        print("Starting run3()", file=sys.stderr)
        
        # Run 3

        # Returning to masterProgram(), resetting display.
        PrintRunNumbersToDisplay()

        
def Trun4A():
    motorStall('A', -15, -7)
    motorStall('D', -10, -7)
    BackMotor.on_for_degrees(10, 60)
    BackMotorShutdown()

def run4(state):
    if state:
        print("run4() button pressed", file=sys.stderr)  
        sound.beep()
        # Clear the first 2 rows of text on the LCD screen using the lcd.rectangle function
        lcd.rectangle(False, x1=0, y1=0, x2=177, y2=39, fill_color='white',outline_color='white')
        lcd.text_pixels("RUN 4", clear_screen=False, x=0, y=0, text_color='black', font=DisplayFont)
        lcd.update()
        print("Starting run1()", file=sys.stderr)

        #########################################################
        # RUN 4: ?? Points
        #########################################################

        # M02: Oil Platform - Pump the Oil - 15 Points for 3 Fuel Units in the Fuel Truck
        run4A = Thread(target=Trun4A)
        run4A.start()
        move_steering.on_for_degrees(0, 30, 180)    
        turnLineDetect('B', 25, 2, 'Black', True)
        turnLineDetect('C', 15, 2, 'Black', False)
        turnLineDetect('C', 15, 2, 'White', True)
        PLF_LineDetect1(2, -1, True)
        RWheel.on_for_degrees(20, 340)
        RWheelShutdown()
        FrontMotor.on_for_degrees(25, 100)
        FrontMotor.on_for_degrees(-25, 100)
        FrontMotor.on_for_degrees(25, 100)
        FrontMotor.on_for_degrees(-25, 100)
        FrontMotor.on_for_degrees(25, 100)
        FrontMotor.on_for_degrees(-25, 100)
        FrontMotorShutdown()
        # M03: Energy Storage - Put 3 Energy Units Into the Energy Storage Bin, Remove Energy Storage Tray - 30 points 10 x 3 energy units
        # 5 points for removing tray from Energy Storage model.
        lineSquare(-15, "Black", "Left", 0.2)
        lineSquare(-15, "White", "Left", 0.2)
        RWheel.on_for_degrees(20, 180)
        RWheelShutdown()
        driveStraight(20, 45, True)
        RWheel.on_for_degrees(20, 195)
        RWheelShutdown()
        driveStraight(-20, 80, True)
        BackMotor.on_for_degrees(-20, 37)
        BackMotorShutdown()
        move_steering.on_for_degrees(12, 80, 1600)
        # move_steering.off()
        WheelShutdown()

        # Returning to masterProgram(), resetting display.
        PrintRunNumbersToDisplay()


def run5(state):
    if state:
        print("run5() button pressed", file=sys.stderr)  
        sound.beep()
        # Clear the first 2 rows of text on the LCD screen using the lcd.rectangle function
        lcd.rectangle(False, x1=0, y1=0, x2=177, y2=39, fill_color='white',outline_color='white')
        lcd.text_pixels("RUN 5", clear_screen=False, x=0, y=0, text_color='black', font=DisplayFont)
        lcd.update()
        print("Starting run5()", file=sys.stderr)

        #########################################################
        # RUN 5: ?? Points
        #########################################################


        sound.set_volume(pct=40)
        sound.play_file('/home/robot/sounds/fanfare.wav', volume=100)

        # Returning to masterProgram(), resetting display.
        PrintRunNumbersToDisplay()
