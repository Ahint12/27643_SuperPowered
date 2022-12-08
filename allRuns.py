#!/usr/bin/env python3
# 
# Filename: allRuns.py
#

import os
import sys
from time import sleep, time

from defineRobot import *
from myBlocks import *

def Trun1A():
    motorStall('A', 15, 12)
    motorStall('D', 7, 5)

def Trun1B():
    motorStall('A', -10, -7)

def Run1_Thread():
    if (True):

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
        twoWheelTurn('Right', 170, 3500, 70)
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


def Run2_Thread():
    if (True):
        
        #########################################################
        # RUN 2: ?? Points
        #########################################################

        #####
        # M08: Watch Television - 20 points
        #####
        driveStraight(35, 470, True)
        driveStraight(20, 70, True)

        #####
        # M07: Wind Turbine - 30 points
        #####
        driveStraight(-25, 150, True)
        RWheel.on_for_degrees(25, 195)
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


def Run3_Thread():
    if (True):
        
        #########################################################
        # RUN 3: ?? Points
        #########################################################

        driveStraight(35, 230, True)
        twoWheelTurn('Left', 170, 3500, 76)
        driveStraight(40, 100, False)
        driveStraight(50, 900, False)
        lineSquare(15, 'Black', 'Right', 0.2)
        lineSquare(15, 'White', 'Left', 0.2)
        WheelShutdown()
        oneWheelTurn('Left', 170, 2000, 338)
        driveStraight(40, 182, True)
        oneWheelTurn('Right', 170, 3500, 162)
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
        driveStraight(35, 215, True)
        oneWheelTurn('Right', 170, 3500, 290)
        driveStraight(80, 350, False)
        move_steering.on_for_degrees(7, 80, 1500)
        WheelShutdown()

        # Return to masterProgram(), reset display
        PrintRunNumbersToDisplay()

        
def Trun4A():
    motorStall('A', -15, -7)
    motorStall('D', -10, -7)
    BackMotor.on_for_degrees(10, 60)
    BackMotorShutdown()

def Run4_Thread():
    if (True):

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
        # M03: Energy Storage - 35 points - 10 x 3 energy units + 5 points for removing tray
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
        move_steering.on_for_degrees(12, 80, 1900)
        WheelShutdown()

        # Return to masterProgram(), reset display
        PrintRunNumbersToDisplay()


def Trun5A():
    motorStall('A', 15, 10)

def Run5_Thread():
    if (True):

        #########################################################
        # RUN 5: ?? Points
        #########################################################

        #####
        # M01: Innovation Project & M13: Power-To-X
        #####
        run5A = Thread(target=Trun5A)
        run5A.start()
        driveStraight(45, 1300, True)
        driveStraight(-30, 300, True) 

        #####
        # M12: Water Reservoir
        #####
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


def Run1(state):
    if state:
        print("Run1 button pressed", file=sys.stderr)  
        sound.beep()
        # Clear the first 2 rows of text on the LCD screen using the lcd.rectangle function
        lcd.rectangle(False, x1=0, y1=0, x2=177, y2=39, fill_color='white',outline_color='white')
        lcd.text_pixels("RUN 1", clear_screen=False, x=0, y=0, text_color='black', font=DisplayFont)
        lcd.update()

        t = multiprocessing.Process(target=Run1_Thread)
        t.start()

        while True:
            if btn.any():
                sound.beep()
                print("Run Abort button pressed", file=sys.stderr)  
                t.terminate()
                WheelShutdown()
                break
            if (not t.is_alive()): 
                print("Run1_Thread successfully completed, exiting", file=sys.stderr)  
                break 
            sleep(0.5)

        PrintRunNumbersToDisplay()


def Run2(state):
    if state:
        print("Run2 button pressed", file=sys.stderr)  
        sound.beep()
        # Clear the first 2 rows of text on the LCD screen using the lcd.rectangle function
        lcd.rectangle(False, x1=0, y1=0, x2=177, y2=39, fill_color='white',outline_color='white')
        lcd.text_pixels("RUN 2", clear_screen=False, x=0, y=0, text_color='black', font=DisplayFont)
        lcd.update()

        t = multiprocessing.Process(target=Run2_Thread)
        t.start()

        while True:
            if btn.any():
                sound.beep()
                print("Run Abort button pressed", file=sys.stderr)  
                t.terminate()
                WheelShutdown()
                break
            if (not t.is_alive()): 
                print("Run2_Thread successfully completed, exiting", file=sys.stderr)  
                break 
            sleep(0.5)

        PrintRunNumbersToDisplay()


def Run3(state):
    if state:
        print("Run3 button pressed", file=sys.stderr)  
        sound.beep()
        # Clear the first 2 rows of text on the LCD screen using the lcd.rectangle function
        lcd.rectangle(False, x1=0, y1=0, x2=177, y2=39, fill_color='white',outline_color='white')
        lcd.text_pixels("RUN 3", clear_screen=False, x=0, y=0, text_color='black', font=DisplayFont)
        lcd.update()

        t = multiprocessing.Process(target=Run3_Thread)
        t.start()

        while True:
            if btn.any():
                sound.beep()
                print("Run Abort button pressed", file=sys.stderr)  
                t.terminate()
                WheelShutdown()
                break
            if (not t.is_alive()): 
                print("Run3_Thread successfully completed, exiting", file=sys.stderr)  
                break 
            sleep(0.5)

        PrintRunNumbersToDisplay()


def Run4(state):
    if state:
        print("Run4 button pressed", file=sys.stderr)  
        sound.beep()
        # Clear the first 2 rows of text on the LCD screen using the lcd.rectangle function
        lcd.rectangle(False, x1=0, y1=0, x2=177, y2=39, fill_color='white',outline_color='white')
        lcd.text_pixels("RUN 4", clear_screen=False, x=0, y=0, text_color='black', font=DisplayFont)
        lcd.update()

        t = multiprocessing.Process(target=Run4_Thread)
        t.start()

        while True:
            if btn.any():
                sound.beep()
                print("Run Abort button pressed", file=sys.stderr)  
                t.terminate()
                WheelShutdown()
                break
            if (not t.is_alive()): 
                print("Run4_Thread successfully completed, exiting", file=sys.stderr)  
                break 
            sleep(0.5)

        PrintRunNumbersToDisplay()


def Run5(state):
    if state:
        print("Run5 button pressed", file=sys.stderr)  
        sound.beep()
        # Clear the first 2 rows of text on the LCD screen using the lcd.rectangle function
        lcd.rectangle(False, x1=0, y1=0, x2=177, y2=39, fill_color='white',outline_color='white')
        lcd.text_pixels("RUN 5", clear_screen=False, x=0, y=0, text_color='black', font=DisplayFont)
        lcd.update()

        t = multiprocessing.Process(target=Run5_Thread)
        t.start()

        while True:
            if btn.any():
                sound.beep()
                print("Run Abort button pressed", file=sys.stderr)  
                t.terminate()
                WheelShutdown()
                break
            if (not t.is_alive()): 
                print("Run5_Thread successfully completed, exiting", file=sys.stderr)  
                break 
            sleep(0.5)

        PrintRunNumbersToDisplay()