#!/usr/bin/env python3
# 
# Filename: defineRobot.py
#

import os
import sys
# import config

from threading import Thread
from time import sleep, time
from math import *

# Import all Motors, Output Ports, and Functions
from ev3dev2.motor import LargeMotor, OUTPUT_B, OUTPUT_C, OUTPUT_D
from ev3dev2.motor import MediumMotor, OUTPUT_A
from ev3dev2.motor import MoveTank, MoveSteering
from ev3dev2.motor import SpeedPercent, SpeedRPS, SpeedDPS
from ev3dev2.motor import SpeedDPS, SpeedRPS, SpeedPercent

# Import all Sensors, Inputs Ports, and Functions
from ev3dev2.sensor import INPUT_2, INPUT_3
from ev3dev2.sensor.lego import ColorSensor
'''
from ev3dev2.sensor.lego import GyroSensor
from ev3dev2.sensor.lego import UltrasonicSensor
from ev3dev2.sensor.lego import TouchSensor
from ev3dev2.sensor.lego import InfraredSensor
'''

# Import all the remaining EV3 Brick pieces
from ev3dev2.display import Display
from ev3dev2.button import Button
from ev3dev2.led import Leds
from ev3dev2.sound import Sound 

# Define Wheel Motor Configurations
LWheel = LargeMotor(OUTPUT_B)
RWheel = LargeMotor(OUTPUT_C)
move_tank = MoveTank(OUTPUT_B, OUTPUT_C)
move_steering = MoveSteering(OUTPUT_B, OUTPUT_C)

# Define Attachment Motor Configurations
FrontMotor = MediumMotor(OUTPUT_A)
BackMotor = LargeMotor(OUTPUT_D)

# Define Sensor Configurations
LColor = ColorSensor(INPUT_2)
RColor = ColorSensor(INPUT_3)
# us = UltrasonicSensor(INPUT_1)
# gs = GyroSensor(INPUT_4)

# Define Button Configurations
btn = Button()

# Define LED Configurations
leds = Leds()

# Define Display Configurations
lcd = Display()
DisplayFont = "lutBS18"  # Used by lcd.text_pixels(), each character is 11x20 pixels
font = DisplayFont
os.system('setfont Lat15-TerminusBold20x10')  # Used by print()

# Define Sound Configurations
sound = Sound()

# Create empty BrickName & RunNumber variables
brick_name = ""
run_number = 1

# Names for the EV3 Bricks used by 2019 Lego Legends
Brick_Names = ["ASHBOT", "NIKBOT"]

# Set the Wheel Diameter in millimeters
WheelDiameter = 62.4

# Kg Values for every Run for each Bot
Bot1_Kg = [3,3,3,3,3]
Bot2_Kg = [3,3,3,3,3]

# For each Bot, define Color Sensor Threshhold Values + Kg values for Gyro-based driving
# ASHBOT
Kg = 1.5
LeftBlackThresholdValue = 12
LeftWhiteThresholdValue = 60
RightBlackThresholdValue = 12
RightWhiteThresholdValue = 60

# NIKBOT
# Kg = 1.5
# LeftBlackThresholdValue = 12
# LeftWhiteThresholdValue = 75
# RightBlackThresholdValue = 10
# RightWhiteThresholdValue = 50

LColor_threshold_midpoint = (LeftBlackThresholdValue + LeftWhiteThresholdValue) / 2
RColor_threshold_midpoint = (RightBlackThresholdValue + RightWhiteThresholdValue) / 2
