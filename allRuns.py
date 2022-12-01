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
    motorStall('A', 15, 12)
    motorStall('D', 7, 5)

def Trun1B():
    motorStall('A', -10, -7)

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

        #####
        # M11: Hydroelectric Dam - 20 Points
        #####
        run1A = Thread(target=Trun1A)
        run1A.start()
        driveStraight(30, 390, True)
        motorStall('A', -20, -15)
        driveStraight(-10, 40, True)
        run1B = Thread(target=Trun1B)
        run1B.start()
        driveStraight(20, 70, True)

        #####
        # M10: Power Plant - 25 Points
        #####
        driveStraight(-25, 55, True)
        twoWheelTurn('Right', 170, 3500, 79)
        driveStraight(35, 100, False)
        driveStraight(45, 100, False)
        driveStraight(50, 700, False)
        lineSquare(15, 'Black', 'Right', 0.2)
        lineSquare(15, 'White', 'Left', 0.15)
        WheelShutdown()
        twoWheelTurn('Right', 170, 3500, 170)
        lineSquare(15, 'Black', 'Left', 0.25)
        lineSquare(-15, 'White', 'Right', 0.15)
        lineSquare(15, 'Black', 'Left', 0.1)
        driveStraight(30, 30, True)
        WheelShutdown()
        sleep(0.1)
        FrontMotor.on_for_degrees(95, 125)
        motorStall('A', 15, 12)
        driveStraight(-10, 15, True)
        LWheel.on_for_degrees(-15, 45, True)
        WheelShutdown()
        FrontMotor.on_for_degrees(-35, 100)
        sleep(0.6)
        FrontMotorShutdown()

        #####
        # M05: Smart Grid - 20 points (30 points if other team raises their hand)
        #####
        LWheel.on_for_degrees(15, 45, True)
        WheelShutdown()
        driveStraight(20, 20, True)
        lineSquare(-15, 'White', 'Left', 0.3)
        lineSquare(15, 'Black', 'Right', 0.2)
        lineSquare(-15, 'White', 'Left', 0.2)
        # driveStraight(-45, 870, True)
        driveStraight(-40, 100, False)
        driveStraight(-50, 760, True)
        motorStall('D', -20, -17)
        driveStraight(15, 100, True)
        BackMotor.on_for_degrees(30, 50)
        BackMotorShutdown()
        driveStraight(80, 400, True)
        RWheel.on_for_degrees(35, 260, True)
        driveStraight(80, 1800, True)
        WheelShutdown()

        # Return to masterProgram(), reset display
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
        WheelSetup()
        FrontMotorSetup()
        BackMotorSetup()
        #####
        # M08: Watch Television - 20 points
        #####
        driveStraight(35, 470, True)
        driveStraight(20, 70, True)
        #####
        # M07: Wind Turbine - 30 points
        #####
        driveStraight(-25, 160, True)
        RWheel.on_for_degrees(25, 205)
        RWheelShutdown()
        driveStraight(35, 400, False)
        lineDetect(15, 3, "Black", False)
        lineDetect(15, 3, "White", True)
        LWheel.on_for_degrees(25, 360)
        LWheelShutdown()
        driveStraight(20, 220, True)
        sleep(0.1)
        driveStraight(-20, 90, True)
        driveStraight(20, 210, True)
        sleep(0.1)
        driveStraight(-20, 90, True)
        driveStraight(20, 220, True)
        sleep(0.1)
        driveStraight(-20, 90, True)
        driveStraight(20, 230, True)
        sleep(0.1)

        #####
        # M14: Toy Factory - 30 points
        #####
        # driveStraight(-20, 150, True)
        # driveStraight(-30, 250, True)
        driveStraight(-30, 290, False)
        driveStraight(-15, 50, True)
        sleep(0.5)
        RWheel.on_for_degrees(25, 140)
        RWheelShutdown()
        LWheel.on_for_degrees(-25, 150)  
        LWheelShutdown()
        driveStraight(-70, 1050, True)

        # Return to masterProgram(), reset display
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
        
        #########################################################
        # RUN 3: ?? Points
        #########################################################

        driveStraight(35, 230, True)
        twoWheelTurn('Left', 170, 3500, 85)
        driveStraight(40, 100, False)
        driveStraight(50, 900, False)
        lineSquare(15, 'Black', 'Right', 0.2)
        lineSquare(15, 'White', 'Left', 0.2)
        WheelShutdown()
        oneWheelTurn('Left', 170, 3500, 350)
        driveStraight(40, 160, True)
        oneWheelTurn('Right', 170, 3500, 172)
        driveStraight(35, 280, True)
        twoWheelTurn('Right', 170, 3500, 75)
        driveStraight(35, 150, True)
        lineSquare(15, 'Black', 'Right', 0.3)
        lineSquare(15, 'White', 'Left', 0.2)
        lineSquare(-15, 'Black', 'Right', 0.15)
        WheelShutdown()
        oneWheelTurn('Right', 170, 3500, 45)
        driveStraight(35, 240, True)
        oneWheelTurn('Right', 170, 3500, 260)
        WheelShutdown()
        driveStraight(35, 230, True)
        oneWheelTurn('Right', 170, 3500, 295)
        driveStraight(80, 1800, True)
        WheelShutdown()

        # Return to masterProgram(), reset display
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

        #####
        # M02: Oil Platform - Pump the Oil - 15 Points for 3 Fuel Units in the Fuel Truck
        #####
        run4A = Thread(target=Trun4A)
        run4A.start()
        move_steering.on_for_degrees(0, 30, 180)    
        turnLineDetect('B', 25, 2, 'Black', True)
        turnLineDetect('C', 15, 2, 'Black', False)
        turnLineDetect('C', 15, 2, 'White', True)
        PLF_Degrees1(2, -1, 500, False)
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
        #####
        # M03: Energy Storage - Put 3 Energy Units Into the Energy Storage Bin, Remove Energy Storage Tray - 30 points 10 x 3 energy units
        # 5 points for removing tray from Energy Storage model.
        #####
        lineSquare(-15, "Black", "Left", 0.2)
        lineSquare(-15, "White", "Left", 0.2)
        driveStraight(-15, 20, True)
        RWheel.on_for_degrees(20, 180)
        RWheelShutdown()
        driveStraight(20, 55, True)
        RWheel.on_for_degrees(20, 185)
        RWheelShutdown()
        driveStraight(-20, 90, True)
        BackMotor.on_for_degrees(-20, 37)
        BackMotorShutdown()
        move_steering.on_for_degrees(12, 80, 2000)
        # move_steering.off()
        WheelShutdown()

        # Return to masterProgram(), reset display
        PrintRunNumbersToDisplay()


def Trun5A():
    motorStall('A', 15, 10)

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
        run5A = Thread(target=Trun5A)
        run5A.start()
        driveStraight(45, 1400, True)
        driveStraight(-30, 300, True) 
        move_tank.on_for_degrees(-15, 15, 165, True)
        WheelShutdown()
        driveStraight(30, 110, True)
        driveStraight(-20, 50, True)
        FrontMotor.on_for_degrees(-10, 100)
        FrontMotorShutdown()
        driveStraight(-30, 250, True)

        sound.set_volume(pct=100)
        # sound.play_file('/home/robot/sounds/NeverGonnaGive.wav', volume=100)
        sound.play_file('/home/robot/sounds/fanfare.wav', volume=100)

        # Return to masterProgram(), reset display
        PrintRunNumbersToDisplay()
