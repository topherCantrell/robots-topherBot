import board
import busio
import time
import json
import pwmio
from adafruit_motor import motor
import digitalio
import neopixel
import adafruit_lsm303dlh_mag
import math

i2c = busio.I2C(board.GP27,board.GP26)
sensor = adafruit_lsm303dlh_mag.LSM303DLH_Mag(i2c)

pixels = neopixel.NeoPixel(board.GP18,2) # 2 pixels. we use the [0]
pixels.fill(0)

# Wait on button GP20
btn20 = digitalio.DigitalInOut(board.GP20)
btn20.direction = digitalio.Direction.INPUT
btn20.pull = digitalio.Pull.UP
pixels[0] = (0,0,80)
while btn20.value: # True until pressed because of pull-up
    time.sleep(0.1)    

time.sleep(2) # Let the user get their fingers away 

m1a = pwmio.PWMOut(board.GP8, frequency=50)
m1b = pwmio.PWMOut(board.GP9, frequency=50)
motor1 = motor.DCMotor(m1a, m1b)
m2a = pwmio.PWMOut(board.GP10, frequency=50)
m2b = pwmio.PWMOut(board.GP11, frequency=50)
motor2 = motor.DCMotor(m2a, m2b)
motor1.throttle = 0.5  # Forward half-speed
motor2.throttle = -0.5 # Backward half-speed

# Taken from "L_Base_no_power_north.json"
OFFSET_X = -34.500
OFFSET_Y = -41.591
SCALE_X = 0.9890
SCALE_Y = 1.0112

def correct(x,y):
    x = (x-OFFSET_X) * SCALE_X
    y = (y-OFFSET_Y) * SCALE_Y
    return (x,y)

def get_current_heading():
    mag_x, mag_y, _ = sensor.magnetic
    degrees_temp = math.atan2(mag_x, mag_y)/math.pi*180

def turn_to(h):
    h = (h % 360) + 360 # starting at 0->360 to avoid negatives


pixels[0] = (80,0,0) # Red LED ... we are moving

turn_to(heading)

pixels[0] = (80,0,0) # Green LED ... we are done