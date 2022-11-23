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


# Release all motor brakes so that wheels and attachments can be adjusted between Runs
def ReleaseAllBrakes():
    LWheel.off(brake = False)
    RWheel.off(brake = False)
    FrontMotor.off(brake = False)
    BackMotor.off(brake = False)


def PrintRunNumbersToDisplay():
    # Release all motor brakes between Runs to make it easy to change attachments
    ReleaseAllBrakes()
    # Clear the first 2 rows of text on the LCD screen using the lcd.rectangle function
    lcd.rectangle(False, x1=0, y1=0, x2=177, y2=39, fill_color='white',outline_color='white')
    lcd.text_pixels("PUSH BUTTON", clear_screen=False, x=0, y=0, text_color='black', font=DisplayFont)
    lcd.text_pixels("FOR RUNS 1-5", clear_screen=False, x=0, y=20, text_color='black', font=DisplayFont)
    lcd.update()
    sound.set_volume(pct=40)
    sound.play_file('/home/robot/sounds/ready.wav', volume=40)


# Set values for the Large Motors driving the wheels 
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
	BackMotor.wait_until_not_moving()
	BackMotor.off(brake = True)   


# One wheel turn that stops when the requested Color Sensor sees the requested color
def turnTankLineDetect(TurnLeftOrRight, Speed, ColorSensorPort, FindBlackOrWhite, StopAtEnd):

    if (TurnLeftOrRight == 'Left'):
        move_tank.on(Speed * -1, Speed)
    elif (TurnLeftOrRight == 'Right'):
        move_tank.on(Speed, Speed * -1)
    
    # Searching on Left Color Sensor
    if (ColorSensorPort == 2):
        if (FindBlackOrWhite == 'Black'):
            while (LColor.reflected_light_intensity >= LeftBlackThresholdValue):
                sleep(0.01)
        if (FindBlackOrWhite == 'White'):
            while (LColor.reflected_light_intensity <= LeftWhiteThresholdValue):
                sleep(0.01)

    # Searching on Right Color Sensor
    if (ColorSensorPort == 3):
        if (FindBlackOrWhite == 'Black'):
            while (RColor.reflected_light_intensity >= RightBlackThresholdValue):
                sleep(0.01)
        if (FindBlackOrWhite == 'White'):
            while (RColor.reflected_light_intensity <= RightWhiteThresholdValue):
                sleep(0.01)

    if (StopAtEnd):
        WheelShutdown()


# Two wheel turn that stops when the requested Color Sensor sees the requested color
def turnLineDetect(MotorPort, Speed, ColorSensorPort, FindBlackOrWhite, StopAtEnd):

    if (MotorPort == 'B'):
        LWheel.on(Speed)
    elif (MotorPort == 'C'):
        RWheel.on(Speed)
    
    # Searching on Left Color Sensor
    if (ColorSensorPort == 2):
        if (FindBlackOrWhite == 'Black'):
            while (LColor.reflected_light_intensity >= LeftBlackThresholdValue):
                sleep(0.01)
        if (FindBlackOrWhite == 'White'):
            while (LColor.reflected_light_intensity <= LeftWhiteThresholdValue):
                sleep(0.01)

    # Searching on Right Color Sensor
    if (ColorSensorPort == 3):
        if (FindBlackOrWhite == 'Black'):
            while (RColor.reflected_light_intensity >= RightBlackThresholdValue):
                sleep(0.01)
        if (FindBlackOrWhite == 'White'):
            while (RColor.reflected_light_intensity <= RightWhiteThresholdValue):
                sleep(0.01)

    if (StopAtEnd):
        WheelShutdown()


# Slow speed Proportional Line Follower
def PLF_Degrees1(LineFollowerPort, BlackLineSide, Degrees, StopAtEnd):

    # Reset the degrees on both Large Motors to 0 and calculate RLI value to follow the Black/White boundary 
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

    if (StopAtEnd):
        WheelShutdown()


# Medium speed Proportional Line Follower
def PLF_Degrees2(LineFollowerPort, BlackLineSide, Degrees, StopAtEnd):

    # Reset the degrees on both Large Motors to 0 and calculate RLI value to follow the Black/White boundary 
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

    if (StopAtEnd):
        WheelShutdown()


# High speed Proportional Line Follower
def PLF_Degrees3(LineFollowerPort, BlackLineSide, Degrees, StopAtEnd):

    # Reset the degrees on both Large Motors to 0 and calculate RLI value to follow the Black/White boundary 
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

    if (StopAtEnd):
        WheelShutdown()


# Low speed Proportional Line Follower, stop driving when the other Color Sensor finds the requested Line Color
def PLF_LineDetect1(LineFollowerPort, BlackLineSide, StopAtEnd):

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

    if (StopAtEnd):
        WheelShutdown()
  

# Run the requested motor as far as it will go, stop the motor when it cannot move any more
def motorStall(MotorPort, Speed, StallSpeed):

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
        

# Drive straight, forward or backward, until the requested Color Sensor find the requested line color
def lineDetect(Speed, ColorSensorPort, FindBlackOrWhite, StopAtEnd):

    move_steering.on(0, Speed)

    # Searching on Left Color Sensor
    if (ColorSensorPort == 2):
        if (FindBlackOrWhite == 'Black'):
            while (LColor.reflected_light_intensity >= LeftBlackThresholdValue):
                sleep(0.001)
        if (FindBlackOrWhite == 'White'):
            while (LColor.reflected_light_intensity <= LeftWhiteThresholdValue):
                sleep(0.001)

    # Searching on Right Color Sensor
    if (ColorSensorPort == 3):
        if (FindBlackOrWhite == 'Black'):
            while (RColor.reflected_light_intensity >= RightBlackThresholdValue):
                sleep(0.001)
        if (FindBlackOrWhite == 'White'):
            while (RColor.reflected_light_intensity <= RightWhiteThresholdValue):
                sleep(0.001)

    if (StopAtEnd):
        WheelShutdown()


# Thread run in parallel with the Left Wheel, drive the Right Wheel until the Right Color Sensor finds the requested line color
def lineSquareRight(Speed, FindBlackOrWhite, DelaySide, DelayTime):

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


# Drive the Left Wheel until the Left Color Sensor finds the requested line color
def lineSquare(Speed, FindBlackOrWhite, DelaySide, DelayTime):

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
    sleep(0.2)
    if (DelaySide == 'Left'):
        sleep(DelayTime)


# Drive straight by using the Motor Encorders to keep both wheels moving exactly the same distance
def driveStraight(Speed, Degrees, StopAtEnd):

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

    if (StopAtEnd):
        WheelShutdown()
