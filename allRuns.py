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


def run1(state):
    if state:
        print("run1() button pressed", file=sys.stderr)  
        sound.beep()
        # Clear the first 2 rows of text on the LCD screen using the lcd.rectangle function
        lcd.rectangle(False, x1=0, y1=0, x2=177, y2=39, fill_color='white',outline_color='white')
        lcd.text_pixels("RUN 1", clear_screen=False, x=0, y=0, text_color='black', font=DisplayFont)
        lcd.update()
        print("Starting run1()", file=sys.stderr)

        # Run 1


def run2(state):
    if state:
        print("run2() button pressed", file=sys.stderr)  
        sound.beep()
        # Clear the first 2 rows of text on the LCD screen using the lcd.rectangle function
        lcd.rectangle(False, x1=0, y1=0, x2=177, y2=39, fill_color='white',outline_color='white')
        lcd.text_pixels("RUN 2", clear_screen=False, x=0, y=0, text_color='black', font=DisplayFont)
        lcd.update()
        print("Starting run2()", file=sys.stderr)
        

        # Run 2
        # M08: Watch Television - 20 points
        
        driveStraight(40, 640, False)
        driveStraight(20, 70, True)
        # M07: Wind Turbine - 30 points
        driveStraight(-15, 125, True)
        RWheel.on_for_degrees(20, 185)
        RWheelShutdown()
        driveStraight(30, 340, True)
        lineDetect(15, 3, "Black", False)
        lineDetect(15, 3, "White", True)
        driveStraight(15, 90, True)
        LWheel.on_for_degrees(20, 345)
        LWheelShutdown()
        driveStraight(20, 230, True)
        sleep(0.5)
        driveStraight(-20, 70, True)
        driveStraight(20, 80, True)
        sleep(0.5)
        driveStraight(-20, 70, True)
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

        
def Trun4A():
    motorStall('A', -15, -7)
    motorStall('D', 10, 5)

def run4(state):
    if state:
        print("run4() button pressed", file=sys.stderr)  
        sound.beep()
        # Clear the first 2 rows of text on the LCD screen using the lcd.rectangle function
        lcd.rectangle(False, x1=0, y1=0, x2=177, y2=39, fill_color='white',outline_color='white')
        lcd.text_pixels("RUN 1", clear_screen=False, x=0, y=0, text_color='black', font=DisplayFont)
        lcd.update()
        print("Starting run1()", file=sys.stderr)

        # Run4
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
        lineSquare(-15, "Black", "Left", 0.2)
        lineSquare(-15, "White", "Left", 0.2)        
        RWheel.on_for_degrees(20, 345)
        RWheelShutdown()
        BackMotor.on_for_degrees(-20, 100)
        BackMotorShutdown()
        move_steering.on_for_degrees(12, 80, 1400)
        move_steering.off()
        # WheelShutdown()


def run5(state):
    if state:
        print("run5() button pressed", file=sys.stderr)  
        sound.beep()
        # Clear the first 2 rows of text on the LCD screen using the lcd.rectangle function
        lcd.rectangle(False, x1=0, y1=0, x2=177, y2=39, fill_color='white',outline_color='white')
        lcd.text_pixels("RUN 5", clear_screen=False, x=0, y=0, text_color='black', font=DisplayFont)
        lcd.update()
        print("Starting run5()", file=sys.stderr)

        # Run 5



        sound.set_volume(pct=40)
        sound.play_file('/home/robot/sounds/Fanfare.wav', volume=100)
