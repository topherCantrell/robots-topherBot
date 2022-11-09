# this file becomes "code.py"

# Press GPIO21 at startup to make writeable
# Press GPIO20 to start moving 
# (There is a 2 second delay before starting)

import board
import busio
import time
import json
import pwmio
from adafruit_motor import motor
import digitalio
import neopixel
import adafruit_lsm303dlh_mag

# The compass is connected to GROVE6
# SCL = board.GP27
# SDA = board.GP26
#
i2c = busio.I2C(board.GP27,board.GP26)
sensor = adafruit_lsm303dlh_mag.LSM303DLH_Mag(i2c)

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
m1a = pwmio.PWMOut(board.GP8, frequency=50)
m1b = pwmio.PWMOut(board.GP9, frequency=50)
motor1 = motor.DCMotor(m1a, m1b)
m2a = pwmio.PWMOut(board.GP10, frequency=50)
m2b = pwmio.PWMOut(board.GP11, frequency=50)
motor2 = motor.DCMotor(m2a, m2b)
motor1.throttle = 0.5  # Forward half-speed
motor2.throttle = -0.5 # Backward half-speed

pixels[0] = (80,0,0) # Red LED ... we are recording

data = []
for _ in range(300): # 30 seconds of data
    mag_x, mag_y, mag_z = sensor.magnetic # Read the data
    data.append([mag_x, mag_y, mag_z])
    time.sleep(0.1) # Tenth of a second

motor1.throttle = None  # None to spin freely (less power)
motor2.throttle = None

with open('data.txt','w') as f:
    json.dump(data,f) # Write the data as JSON

pixels[0] = (0,80,0) # Green LED ... we are done
