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

'''def Trun1A():
    motorStall('A', 15, 7)
    motorStall('D', 10, 5) 

def Trun1B():
    FrontMotor.on_for_degrees(-30, 80)
    FrontMotorShutdown()

def Trun1C():
    motorStall('A', 15, 7)        

def Trun1D():
    motorStall('A', -20, -10)

def Trun1E():
    motorStall('D', 10, 5)
'''

def Trun1A():
    motorStall('A', -15, -7)
    motorStall('D', 10, 5)

def run1(state):
    if state:
        print("run1() button pressed", file=sys.stderr)  
        sound.beep()
        # Clear the first 2 rows of text on the LCD screen using the lcd.rectangle function
        lcd.rectangle(False, x1=0, y1=0, x2=177, y2=39, fill_color='white',outline_color='white')
        lcd.text_pixels("RUN 1", clear_screen=False, x=0, y=0, text_color='black', font=DisplayFont)
        lcd.update()
        print("Starting run1()", file=sys.stderr)

        # Run1
        # M02: Oil Platform - Pump the Oil - 15 Points for 3 Fuel Units in the Fuel Truck
        run1A = Thread(target=Trun1A)
        run1A.start()
        move_steering.on_for_degrees(0, 30, 180)    
        turnLineDetect('B', 25, 2, 'Black', True)
        turnLineDetect('C', 15, 2, 'Black', False)
        turnLineDetect('C', 15, 2, 'White', True)
        PLF_LineDetect1(2, -1)
        WheelShutdown()
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
        

        driveStraight(60, 775)
        lineDetect(25, 3, 'White', False)
        lineDetect(25, 3, 'Black', False)
        lineDetect(25, 3, 'White', True)
        turnLineDetect('B', 20, 3, 'White', False)
        turnLineDetect('B', 20, 3, 'Black', False)
        turnLineDetect('B', 20, 3, 'White', True)
        RWheel.on_for_degrees(30, 30)
        RWheelShutdown()
        PLF_LineDetect1(3, 1)
        WheelShutdown()
        LWheel.on_for_degrees(30, 24)
        LWheelShutdown()
        driveStraight(55, 255)
        WheelShutdown()
        driveStraight(-30, 20)
        WheelShutdown()
        motorStall('A', 40, 20)
        RWheel.on_for_degrees(-30, 60)
        RWheelShutdown()
        driveStraight(-30, 105)
        WheelShutdown()
        turnLineDetect('B', -25, 2, 'White', True)
        lineSquare(-15, 'Black', 'Left', 0.2)
        LWheel.on_for_degrees(-30, 145)
        LWheelShutdown()
        move_tank.on_for_degrees(-20, 20, 100)
        WheelShutdown()
        driveStraight(-15, 20)
        WheelShutdown()
        motorStall('A', -60, -15)
        motorStall('A', 60, 15)
        driveStraight(25, 30)
        WheelShutdown()
        RWheel.on_for_degrees(25, 170)
        RWheelShutdown()
        move_tank.on_for_degrees(-13, 13, 68)
        driveStraight(25, 10)
        WheelShutdown()
        driveStraight(-25, 145)
        WheelShutdown()
        move_tank.on_for_degrees(-11, 11, 110)
        WheelShutdown()
        driveStraight(85, 1600)
        WheelShutdown()


def Trun3A():
    motorStall('A', -30, -15)
    
def Trun3B():
    # Branch for FrontMotorStall
    run3A = Thread(target=Trun3A)
    run3A.start()
    motorStall('D', 20, 10)

def Trun3C():
    motorStall('D', 20, 10)

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
        # Branch for BackMotorStall
        run3B = Thread(target=Trun3B)
        run3B.start()
        driveStraight(50, 180)
        WheelShutdown()
        turnLineDetect('C', 25, 3,'Black', True)
        turnLineDetect('B', 15, 3, 'Black', False)
        turnLineDetect('B', 15, 3, 'White', True)
        PLF_LineDetect1(3, 1)
        WheelShutdown()
        LWheel.on_for_degrees(35, 184)
        LWheelShutdown()
        driveStraight(45, 90)
        PLF_Degrees2(2, -1, 275)
        WheelShutdown()
        move_tank.on_for_degrees(-20, 20, 180)
        WheelShutdown()
        lineSquare(-15, 'Black', 'Left', 0.3)
        sleep(0.1)
        lineSquare(10, 'White', 'Left', 0.3)
        sleep(0.1)
        driveStraight(45, 265)
        WheelShutdown()
        BackMotor.on_for_degrees(-30, 140)
        BackMotorShutdown()
        driveStraight(45, 155)
        WheelShutdown()
        # Branch for BackMotorStall
        run3C = Thread(target=Trun3C)
        run3C.start()
        sleep(0.3)
        move_tank.on_for_degrees(20, -20, 60)
        WheelShutdown()
        driveStraight(-45, 270)
        WheelShutdown()
        move_tank.on_for_degrees(-20, 20, 75)
        WheelShutdown()
        move_tank.on_for_degrees(25, -25, 185)
        PLF_Degrees1(3, 1, 250)
        PLF_Degrees3(3, 1, 650)
        PLF_LineDetect1(3, 1)
        WheelShutdown()
        sleep(0.1)
        move_tank.on_for_degrees(20, -20, 170)
        WheelShutdown()
        sleep(2)
        lineSquare(-15, 'Black', 'Left', 0.35)
        sleep(2)
        driveStraight(-30, 195)
        WheelShutdown()
        sleep(0.1)
        LWheel.on_for_degrees(-25, 335)
        LWheelShutdown()
        sleep(0.1)
        driveStraight(35, 520)
        WheelShutdown()
        driveStraight(-35, 200)
        WheelShutdown()
        RWheel.on_for_degrees(-30, 70)
        RWheelShutdown()
        driveStraight(35, 170)
        WheelShutdown()
        lineDetect(20, 3, 'White', False)
        lineDetect(20, 3, 'Black', False)
        lineDetect(20, 3, 'White', True)
        turnTankLineDetect('Left', 15, 3, 'White', False)
        turnTankLineDetect('Left', 15, 3, 'Black', True)
        PLF_Degrees1(3, 1, 400)
        WheelShutdown()
        move_tank.on_for_degrees(-25, 25, 145)
        WheelShutdown()
        # sleep(2)
        FrontMotor.on_for_degrees(50, 70)
        FrontMotorShutdown()
        motorStall('A', -30, -15)
        turnTankLineDetect('Right', 12, 3, 'White', False)
        turnTankLineDetect('Right', 12, 3, 'Black', False)
        turnTankLineDetect('Right', 12, 3, 'White', True)
        driveStraight(20, 160)
        WheelShutdown()
        # sleep(2)
        lineDetect(15, 2, 'Black', True)
        sleep(2)
        driveStraight(10, 32)
        WheelShutdown()
        sleep(2)
        LWheel.on_for_degrees(17, 135)
        LWheelShutdown()
        sleep(5)
        move_tank.on_for_degrees(20, -20, 160)
        WheelShutdown()
        driveStraight(-20, 55)
        WheelShutdown()
        FrontMotor.on_for_degrees(30, 95)
        FrontMotorShutdown()
        PLF_Degrees1(2, -1, 150)
        PLF_Degrees3(2, -1, 640)
        WheelShutdown()
        driveStraight(-20, 25)
        WheelShutdown()
        motorStall('A', -30, -15)

        
def Trun4A():
    motorStall('D', 20, 10)


def run4(state):
    if state:
        print("run4() button pressed", file=sys.stderr)  
        sound.beep()
        # Clear the first 2 rows of text on the LCD screen using the lcd.rectangle function
        lcd.rectangle(False, x1=0, y1=0, x2=177, y2=39, fill_color='white',outline_color='white')
        lcd.text_pixels("RUN 4", clear_screen=False, x=0, y=0, text_color='black', font=DisplayFont)
        lcd.update()
        print("Starting run4()", file=sys.stderr)

        # Run 4
        # Branch for BackMotorStall
        run4A = Thread(target=Trun4A)
        run4A.start()
        WheelShutdown()

        driveStraight(35, 270)
        WheelShutdown()
        turnLineDetect('C', 25, 3,'Black', True)
        turnLineDetect('B', 15, 3, 'Black', False)
        turnLineDetect('B', 15, 3, 'White', True)
        PLF_LineDetect1(3, 1)
        WheelShutdown()

        '''
        driveStraight(35, 270)
        WheelShutdown()
        turnLineDetect('C', 30, 3, 'White', False)
        turnLineDetect('C', 30, 3, 'Black', True)
        turnLineDetect('B', 20, 3, 'Black', False)
        turnLineDetect('C', 30, 3, 'White', True)
        PLF_LineDetect1(3, 1)
        WheelShutdown()
        '''

        driveStraight(40, 235)
        WheelShutdown()
        LWheel.on_for_degrees(25, 175)
        LWheelShutdown()
        PLF_Degrees1(3, 1, 250)
        PLF_Degrees3(3, 1, 325)
        PLF_Degrees2(3, 1, 275)
        PLF_LineDetect1(3, 1)
        WheelShutdown()
        driveStraight(30, 300)
        WheelShutdown()
        LWheel.on_for_degrees(25, 350)
        LWheelShutdown()
        driveStraight(25, 15)
        WheelShutdown()
        motorStall('A', 50, 25)
        driveStraight(-35, 110)
        WheelShutdown()
        LWheel.on_for_degrees(-22, 110)
        LWheelShutdown()
        lineSquare(-15, 'Black', 'Left', 0.3)
        driveStraight(-30, 50)
        WheelShutdown()
        LWheel.on_for_degrees(-22, 240)
        LWheelShutdown()
        driveStraight(-50, 535)
        WheelShutdown()
        lineSquare(-15, 'Black', 'Left', 0.25)
        lineSquare(-15, 'White', 'Left', 0.25)
        driveStraight(-45, 190)
        WheelShutdown()
        driveStraight(25, 15)
        WheelShutdown()
        RWheel.on_for_degrees(20, 390)
        RWheelShutdown()
        driveStraight(60, 550)
        WheelShutdown()
        move_steering.on_for_seconds(0, 35, 0.45)
        WheelShutdown()
        driveStraight(-35, 180)
        WheelShutdown()
        RWheel.on_for_degrees(20, 390)
        RWheelShutdown()
        driveStraight(-20, 30)
        WheelShutdown()
        lineSquare(15, 'Black', 'Left', 0.25)
        lineSquare(-15, 'White', 'Left', 0.25)
        driveStraight(-35, 190)
        WheelShutdown()
        motorStall('D', -10, -5)
        driveStraight(45, 155)
        WheelShutdown()
        lineSquare(20, 'Black', 'Left', 0.25)
        sleep(0.2)
        driveStraight(12, 108)
        WheelShutdown()
        sound.set_volume(pct=40)
        sound.play_file('/home/robot/sounds/Fanfare.wav', volume=100)
