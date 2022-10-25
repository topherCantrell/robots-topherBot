# this file becomes "code.py"

# Press GPIO21 at startup to make writeable
# Press GPIO20 to start recording (2 second delay before starting)
# Records 30 seconds of data to "data.txt"

import board
import busio
import time
import json
import pwmio
from adafruit_motor import motor
import digitalio
import neopixel

# Copy these files/directories from the circuit-python distribution to the "lib" directory
# on the board:
#
#    adafruit_bus_device
#    adafruit_register
#    adafruit_lsm303_accel.mpy
#    adafruit_lsm303dlh_mag.mpy
#
import adafruit_lsm303dlh_mag

# The compass is connected to GROVE6
# SCL = board.GP27
# SDA = board.GP26
#
i2c = busio.I2C(board.GP27,board.GP26)

pixels = neopixel.NeoPixel(board.GP18,2) # 2 pixels. we use the [0]
pixels.fill(0)

# Wait on button GP20
btn20 = digitalio.DigitalInOut(board.GP20)
btn20.direction = digitalio.Direction.INPUT
btn20.pull = digitalio.Pull.UP
while btn20.value: # True until pressed because of pull-up
    time.sleep(0.1)    

time.sleep(2) # Let the user get their fingers away
  
# Slow spin
# Initialize DC motors
"""
m1a = pwmio.PWMOut(board.GP8, frequency=50)
m1b = pwmio.PWMOut(board.GP9, frequency=50)
motor1 = motor.DCMotor(m1a, m1b)
m2a = pwmio.PWMOut(board.GP10, frequency=50)
m2b = pwmio.PWMOut(board.GP11, frequency=50)
motor2 = motor.DCMotor(m2a, m2b)
motor1.throttle = 1.0  # motor1.throttle = 1 or -1 for full speed
motor2.throttle = -1.0
"""

sensor = adafruit_lsm303dlh_mag.LSM303DLH_Mag(i2c)
data = []

pixels[0] = (80,0,0) # Red ... we are recording

for _ in range(300): # 30 seconds of data
    mag_x, mag_y, mag_z = sensor.magnetic
    data.append([mag_x, mag_y, mag_z])
    time.sleep(0.1) # Tenth of a second

"""
motor1.throttle = None  # motor1.throttle = None to spin freely (less power)
motor2.throttle = None
"""

with open('data.txt','w') as f:
    json.dump(data,f)

pixels[0] = (0,80,0) # Green ... we are done
