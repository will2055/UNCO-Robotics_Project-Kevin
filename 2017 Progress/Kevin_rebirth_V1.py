# -*- coding: utf-8 -*-
import time
import serial

#Initialize serial communication

s = serial.Serial("/dev/ttyAMA0", 38400, timeout=0.5)

#Motor Definitions
#
#0xAA, 0x09, motorID, 0x7f
#s.write( chr(0xAA) + chr(0x09) + chr(0x08) + chr(0x7F) )
#
#Motor 0: 0x08 forward, 0x0A reverse
#
#Motor 1: 0x0C forward, 0x0E reverse

#Initialize ADC module
time.sleep(3)

import Adafruit_ADS1x15

def motor_forward():
	#M0 right Side
        s.write( chr(0xAA) + chr(0x09) + chr(0x0A) + chr(0x40))
        #M1 left Side
        s.write( chr(0xAA) + chr(0x09) + chr(0x0C) + chr(0x40))

def motor_reverse():
	#M0 Right Side
	s.write( chr(0xAA) + chr(0x09) + chr(0x08) + chr(0x40))
	#M1 Left Side
	s.write( chr(0xAA) + chr(0x09) + chr(0x0E) + chr(0x40))
	print(1)
def right_turn():
	#M0 Right Side
	s.write( chr(0xAA) + chr(0x09) + chr(0x08) + chr(0x40))
	#M1 Left Side
	s.write( chr(0xAA) + chr(0x09) + chr(0x0C) + chr(0x40))
	print(2)
def left_turn():
	#M0 Right Side
	s.write( chr(0xAA) + chr(0x09) + chr(0x0A) + chr(0x40))
	#M1 Left Side
	s.write( chr(0xAA) + chr(0x09) + chr(0x0E) + chr(0x40))
	print(3)
def motor_stop():
	s.write( chr(0xAA) + chr(0x09) + chr(0x0A) + chr(0x00))
	s.write( chr(0xAA) + chr(0x09) + chr(0x0C) + chr(0x00))
	print(4)
adc = Adafruit_ADS1x15.ADS1115()
GAIN = 1
#Define Sensors
leftSensor= adc.read_adc(0, gain=GAIN)
midSensor= adc.read_adc(1, gain=GAIN)
rightSensor= adc.read_adc(2, gain=GAIN)
bottomSensor= adc.read_adc(3, gain=GAIN)

time.sleep(.5)
motor_forward()
while True:
    leftSensor= adc.read_adc(0, gain=GAIN)
    midSensor= adc.read_adc(1, gain=GAIN)
    rightSensor= adc.read_adc(2, gain=GAIN)
    bottomSensor= adc.read_adc(3, gain=GAIN)

    if(leftSensor<15000 & midSensor<15000 &
       rightSensor<15000 & bottomSensor<18000):
        #Set motors to drive forward
	motor_forward()
    if(leftSensor>=15000):
        #Stop, Reverse, turn right, drive
        motor_stop()
	time.sleep(.5)
	motor_reverse()
	time.sleep(.6)
	right_turn()
	time.sleep(.6)
	motor_forward()
    if(midSensor>=15000):
        #Stop, Reverse, turn right, drive 
	motor_stop()
	time.sleep(.5)
	motor_reverse()
	time.sleep(.6)
	right_turn()
	time.sleep(.6)
	motor_forward()
    if(rightSensor>=15000):
        #Stop, Reverse, turn left, drive
        motor_stop()
	time.sleep(.5)
	motor_reverse()
	time.sleep(.6)
	left_turn()
	time.sleep(.6)
	motor_forward()
    if(bottomSensor>=17000):
        #Stop, Reverse, turn right, drive
        motor_stop()
	time.sleep(.5)
	motor_reverse()
	time.sleep(.6)
	right_turn()
	time.sleep(.6)
	motor_forward()
s.close()
