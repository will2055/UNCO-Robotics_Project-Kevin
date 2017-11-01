import time
import serial

s=serial.Serial(¨dev/ttyAMA0¨, 38400, timeout=0.5)
s.write(chr(0xAA) + chr(0x09) + chr(0x7F))
time.sleep(2)
s.write(chr(0xAA)+chr(0x09)+chr(0x0A)+chr(0x00))
s.close()
