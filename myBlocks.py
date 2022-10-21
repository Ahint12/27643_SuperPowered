#!/usr/bin/env python3
# 
# Filename: myBlocks.py
#

import os
import sys
import multiprocessing
# import config

from queue import Queue
from time import sleep, time
from defineRobot import *


# Set values for the LargeMotors driving the wheels 
def WheelSetup(): 
	LWheel.stop_action = 'hold'
	LWheel.polarity = 'normal'
	RWheel.stop_action = 'hold'
	RWheel.polarity = 'normal'


# Set values for FrontMotor 
def FrontMotorSetup():
	FrontMotor.stop_action = 'hold'


# Set values for BackMotor
def BackMotorSetup():
	BackMotor.stop_action = 'brake'


# Function to stop the wheels turning after any driving command 
def WheelShutdown():
	LWheel.stop_action = 'hold'
	RWheel.stop_action = 'hold'
	LWheel.stop()
	RWheel.stop()
	LWheel.wait_until_not_moving()
	RWheel.wait_until_not_moving()
	LWheel.stop_action = 'coast'
	RWheel.stop_action = 'coast'
	LWheel.reset()
	RWheel.reset()
	WheelSetup()
	LWheel.off(brake = True)
	RWheel.off(brake = True)


# Function to stop the Left wheel turning after any driving command 
def LWheelShutdown():
	LWheel.stop_action = 'hold'
	LWheel.stop()
	LWheel.wait_until_not_moving()
	LWheel.stop_action = 'coast'
	LWheel.reset()
	WheelSetup()
	LWheel.off(brake = True)


# Function to stop the Right wheel turning after any driving command 
def RWheelShutdown():
	RWheel.stop_action = 'hold'
	RWheel.stop()
	RWheel.wait_until_not_moving()
	RWheel.stop_action = 'coast'
	RWheel.reset()
	WheelSetup()
	RWheel.off(brake = True)    


# Function to stop the FrontMotor turning after any move command 
def FrontMotorShutdown():
	FrontMotor.stop_action = 'brake'
	FrontMotor.stop()
	FrontMotor.wait_until_not_moving()
	FrontMotor.off(brake = True)    


# Function to stop the BackMotor turning after any move command 
def BackMotorShutdown():
	BackMotor.stop_action = 'brake'
	BackMotor.stop()
	# BackMotor.wait_until_not_moving()
	BackMotor.off(brake = True)   


def turnTankLineDetect(TurnLeftOrRight, Speed, ColorSensorPort, FindBlackOrWhite, StopAtEnd):
    # By: Ashten Hintzman

    if (TurnLeftOrRight == 'Left'):
        move_tank.on(Speed * -1, Speed)
    elif (TurnLeftOrRight == 'Right'):
        move_tank.on(Speed, Speed * -1)
    
    # Searching on Left Color Sensor
    if (ColorSensorPort == 2):
        if (FindBlackOrWhite == 'Black'):
            while (LColor.reflected_light_intensity >= LeftBlackThresholdValue):
                sleep(0.01)
            if (StopAtEnd):
                WheelShutdown()
        if (FindBlackOrWhite == 'White'):
            while (LColor.reflected_light_intensity <= LeftWhiteThresholdValue):
                sleep(0.01)
            if (StopAtEnd):
                WheelShutdown()

    # Searching on Right Color Sensor
    if (ColorSensorPort == 3):
        if (FindBlackOrWhite == 'Black'):
            while (RColor.reflected_light_intensity >= RightBlackThresholdValue):
                sleep(0.01)
            if (StopAtEnd):
                WheelShutdown()
        if (FindBlackOrWhite == 'White'):
            while (RColor.reflected_light_intensity <= RightWhiteThresholdValue):
                sleep(0.01)
            if (StopAtEnd):
                WheelShutdown()


def turnLineDetect(MotorPort, Speed, ColorSensorPort, FindBlackOrWhite, StopAtEnd):
    # By: Ashten Hintzman

    if (MotorPort == 'B'):
        LWheel.on(Speed)
    elif (MotorPort == 'C'):
        RWheel.on(Speed)
    
    # Searching on Left Color Sensor
    if (ColorSensorPort == 2):
        if (FindBlackOrWhite == 'Black'):
            while (LColor.reflected_light_intensity >= LeftBlackThresholdValue):
                sleep(0.01)
            if (StopAtEnd):
                WheelShutdown()
        if (FindBlackOrWhite == 'White'):
            while (LColor.reflected_light_intensity <= LeftWhiteThresholdValue):
                sleep(0.01)
            if (StopAtEnd):
                WheelShutdown()

    # Searching on Right Color Sensor
    if (ColorSensorPort == 3):
        if (FindBlackOrWhite == 'Black'):
            while (RColor.reflected_light_intensity >= RightBlackThresholdValue):
                sleep(0.01)
            if (StopAtEnd):
                WheelShutdown()
        if (FindBlackOrWhite == 'White'):
            while (RColor.reflected_light_intensity <= RightWhiteThresholdValue):
                sleep(0.01)
            if (StopAtEnd):
                WheelShutdown()



def PLF_Degrees1(LineFollowerPort, BlackLineSide, Degrees):
    # By: Ashten Hintzman

    # Reset the degrees on both LargeMotors to 0 
    LWheel.position = 0
    RWheel.position = 0
    LColor_threshold_midpoint = (LeftBlackThresholdValue + LeftWhiteThresholdValue) / 2
    RColor_threshold_midpoint = (RightBlackThresholdValue + RightWhiteThresholdValue) / 2

    # Proportional value for the LineFollower 
    Klf = -0.7           

    if (LineFollowerPort == 3):
        # Stop when LWheel has gone the amount of Degrees it needs to.
        while (LWheel.position <= Degrees):
            steering = BlackLineSide * (RColor.reflected_light_intensity - RColor_threshold_midpoint) * Klf
            move_steering.on(steering, 20)

    elif (LineFollowerPort == 2):
        # The condition is still the same, stop when LWheel has gone the amount of Degrees it needs to.
        while (LWheel.position <= Degrees):
            steering = BlackLineSide * (LColor.reflected_light_intensity - LColor_threshold_midpoint) * Klf
            move_steering.on(steering, 20)


def PLF_Degrees2(LineFollowerPort, BlackLineSide, Degrees):
    # By: Ashten Hintzman

    # Reset the degrees on both LargeMotors to 0 
    LWheel.position = 0
    RWheel.position = 0
    LColor_threshold_midpoint = (LeftBlackThresholdValue + LeftWhiteThresholdValue) / 2
    RColor_threshold_midpoint = (RightBlackThresholdValue + RightWhiteThresholdValue) / 2

    # Proportional value for the LineFollower 
    Klf = -0.5           

    if (LineFollowerPort == 3):
        # Stop when LWheel has gone the amount of Degrees it needs to.
        while (LWheel.position <= Degrees):
            steering = BlackLineSide * (RColor.reflected_light_intensity - RColor_threshold_midpoint) * Klf
            move_steering.on(steering, 25)

    elif (LineFollowerPort == 2):
        # The condition is still the same, stop when LWheel has gone the amount of Degrees it needs to.
        while (LWheel.position <= Degrees):
            steering = BlackLineSide * (LColor.reflected_light_intensity - LColor_threshold_midpoint) * Klf
            move_steering.on(steering, 25)


def PLF_Degrees3(LineFollowerPort, BlackLineSide, Degrees):
    # By: Ashten Hintzman

    # Reset the degrees on both LargeMotors to 0 
    LWheel.position = 0
    RWheel.position = 0
    LColor_threshold_midpoint = (LeftBlackThresholdValue + LeftWhiteThresholdValue) / 2
    RColor_threshold_midpoint = (RightBlackThresholdValue + RightWhiteThresholdValue) / 2

    # Proportional value for the LineFollower 
    Klf = -0.15           

    if (LineFollowerPort == 3):
        # Stop when LWheel has gone the amount of Degrees it needs to.
        while (LWheel.position <= Degrees):
            steering = BlackLineSide * (RColor.reflected_light_intensity - RColor_threshold_midpoint) * Klf
            move_steering.on(steering, 45)

    elif (LineFollowerPort == 2):
        # The condition is still the same, stop when LWheel has gone the amount of Degrees it needs to.
        while (LWheel.position <= Degrees):
            steering = BlackLineSide * (LColor.reflected_light_intensity - LColor_threshold_midpoint) * Klf
            move_steering.on(steering, 45)



def PLF_LineDetect1(LineFollowerPort, BlackLineSide):
    # By: Ashten Hintzman

    # Reset the degrees on both LargeMotors to 0 
    LWheel.position = 0
    RWheel.position = 0
    LColor_threshold_midpoint = (LeftBlackThresholdValue + LeftWhiteThresholdValue) / 2
    RColor_threshold_midpoint = (RightBlackThresholdValue + RightWhiteThresholdValue) / 2

    # Proportional value for the LineFollower 
    Klf = -0.7           

    if (LineFollowerPort == 3):
        # Stop when Left Color Sensor sees Black
        LineDetectPort = 2
        while (LColor.reflected_light_intensity >= LeftBlackThresholdValue):
            steering = BlackLineSide * (RColor.reflected_light_intensity - RColor_threshold_midpoint) * Klf
            move_steering.on(steering, 20)

    elif (LineFollowerPort == 2):
        # Stop when Right Color Sensor sees Black
        LineDetectPort = 3
        while (RColor.reflected_light_intensity >= RightBlackThresholdValue):
            steering = BlackLineSide * (LColor.reflected_light_intensity - LColor_threshold_midpoint) * Klf
            move_steering.on(steering, 20)
  

def motorStall(MotorPort, Speed, StallSpeed):
    # By: Ashten Hintzman

    if (MotorPort == 'A'):
        FrontMotor.on(Speed)
        sleep(0.15)
        while ((abs(FrontMotor.speed) * (50 / 780)) >= (abs(StallSpeed))):
            sleep(0.001)
        FrontMotorShutdown()

    elif (MotorPort == 'D'):
        BackMotor.on(Speed)
        sleep(0.08)
        while ((abs(BackMotor.speed) * (50 / 520)) >= (abs(StallSpeed))):
            sleep(0.001)
        BackMotorShutdown()
        

def lineDetect(Speed, ColorSensorPort, FindBlackOrWhite, StopAtEnd):
    # By: Ashten Hintzman

    move_steering.on(0, Speed)

    # Searching on Left Color Sensor
    if (ColorSensorPort == 2):
        if (FindBlackOrWhite == 'Black'):
            while (LColor.reflected_light_intensity >= LeftBlackThresholdValue):
                sleep(0.001)
            if (StopAtEnd):
                WheelShutdown()
        if (FindBlackOrWhite == 'White'):
            while (LColor.reflected_light_intensity <= LeftWhiteThresholdValue):
                sleep(0.001)
            if (StopAtEnd):
                WheelShutdown()

    # Searching on Right Color Sensor
    if (ColorSensorPort == 3):
        if (FindBlackOrWhite == 'Black'):
            while (RColor.reflected_light_intensity >= RightBlackThresholdValue):
                sleep(0.001)
            if (StopAtEnd):
                WheelShutdown()
        if (FindBlackOrWhite == 'White'):
            while (RColor.reflected_light_intensity <= RightWhiteThresholdValue):
                sleep(0.001)
            if (StopAtEnd):
                WheelShutdown()


def lineSquareRight(Speed, FindBlackOrWhite, DelaySide, DelayTime):
    # By: Ashten Hintzman

    RWheel.on(Speed)
    if (FindBlackOrWhite == 'Black'):
        while (RColor.reflected_light_intensity >= RightBlackThresholdValue):
            sleep(0.001)
        RWheelShutdown()
    if (FindBlackOrWhite == 'White'):
        while (RColor.reflected_light_intensity <= RightWhiteThresholdValue):
            sleep(0.001)
        RWheelShutdown()
    if (DelaySide == 'Right'):
        sleep(DelayTime)


def lineSquare(Speed, FindBlackOrWhite, DelaySide, DelayTime):
    # By: Ashten Hintzman

    t = Thread(target=lineSquareRight, args=(Speed, FindBlackOrWhite, DelaySide, DelayTime))
    t.start()

    LWheel.on(Speed)
    if (FindBlackOrWhite == 'Black'):
        while (LColor.reflected_light_intensity >= LeftBlackThresholdValue):
            sleep(0.001)
        LWheelShutdown()
    if (FindBlackOrWhite == 'White'):
        while (LColor.reflected_light_intensity <= LeftWhiteThresholdValue):
            sleep(0.001)
        LWheelShutdown()
    if (DelaySide == 'Left'):
        sleep(DelayTime)


def driveStraight(Speed, Degrees):
    # By: Ashten Hintzman

    LWheel.position = 0
    RWheel.position = 0

    if (Speed >= 0):
        avgDegrees = (fabs(LWheel.position) + fabs(RWheel.position)) / 2
        while (avgDegrees <= Degrees):
            move_steering.on(RWheel.position - LWheel.position, Speed)
            avgDegrees = (fabs(LWheel.position) + fabs(RWheel.position)) / 2
    
    else:
        avgDegrees = (fabs(LWheel.position) + fabs(RWheel.position)) / 2
        while (avgDegrees <= Degrees):
            move_steering.on(LWheel.position - RWheel.position, Speed)
            avgDegrees = (fabs(LWheel.position) + fabs(RWheel.position)) / 2

