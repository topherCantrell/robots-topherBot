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
import simpleio

PIEZO_PIN = board.GP22

i2c = busio.I2C(board.GP27,board.GP26)
sensor = adafruit_lsm303dlh_mag.LSM303DLH_Mag(i2c)

pixels = neopixel.NeoPixel(board.GP18,2) # 2 pixels. we use the [0]
pixels.fill(0)

simpleio.tone(PIEZO_PIN, 400, duration=0.25)
simpleio.tone(PIEZO_PIN, 600, duration=0.25)

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

# Taken from "L_Base_no_power_north.json"
OFFSET_X = -34.500
OFFSET_Y = -41.591
SCALE_X = 0.9890
SCALE_Y = 1.0112
FORWARD = 180.00 # Board is mounted with -Y forward

def correct(x,y):
    x = (x-OFFSET_X) * SCALE_X
    y = (y-OFFSET_Y) * SCALE_Y
    return (x,y)

def get_current_heading():
    # Clockwise: 0=North, 90=east, 180=south, 270=west
    mag_x, mag_y, _ = sensor.magnetic            # Read the sensor
    mag_x = (mag_x-OFFSET_X) * SCALE_X           # Apply the ...
    mag_y = (mag_y-OFFSET_Y) * SCALE_Y           # ... correction
    ret = math.atan2(mag_x, mag_y)/math.pi*180   # Get heading angle
    ret = 360 - ret                              # Reverse so 90=EAST, 270=WEST
    ret = (ret+FORWARD) % 360                    # Offset to robot forward
    return ret

def get_heading_difference(cur,head):
    """get the shortest distance on the compass wheel

       This will always be less than or equal to 180. Positive values
       are distance clockwise. Negative values are distance 
       counter-clockwise.
    """
    distance = head-cur
    if distance<-180:
        distance+=360
    elif distance>180:
        distance-=360
    return distance


def turn_to(heading):
    TURN_SPEED = 0.25
    heading = (heading % 360)    # Just in case
    cur = get_current_heading()  # Current heading
    distance = get_heading_difference(cur,heading) # Current distance to target heading    
    if distance<0: # shortest distance is CCW
        #print('CCW INITIAL DISTANCE,CUR',distance,cur)
        # spinning CCW
        motor1.throttle = -TURN_SPEED
        motor2.throttle = TURN_SPEED
        while distance<0: # Until we first pass the target
            cur = get_current_heading()
            distance = get_heading_difference(cur,heading)    
            #print('CCW DISTANCE,CUR',distance,cur)        
    else: # shortest distance is CW
        #print('CW INITIAL DISTANCE,CUR',distance,cur)
        # spinning CW
        motor1.throttle = TURN_SPEED
        motor2.throttle = -TURN_SPEED
        while distance>0: # Until we first pass the target
            cur = get_current_heading()
            distance = get_heading_difference(cur,heading)       
            #print('CW DISTANCE,CUR',distance,cur)     
    motor1.throttle = None
    motor2.throttle = None


def drive_to(heading,secs):
    log(f'Driving to {heading} for {secs} seconds')
    FULL = .70
    heading = (heading % 360)    # Just in case    
    hunds = secs*4  # 4 times a seconds
    while hunds>0:
        cur = get_current_heading()  # Current heading
        diff = get_heading_difference(cur,heading)        
        cor = diff/180 * 0.50 # 0:180 becomes 0:50%
        cor = cor * FULL  # 0 to 25% reduction        
        if cor>0:  # Turn CCW
            log(f'>CCW cur={cur} diff={diff} cor={cor} left={FULL-abs(cor)} right={FULL}')                     
            motor2.throttle = FULL - abs(cor)  # Reduced
            motor1.throttle = FULL  # Right motor full
        else:  # Turn CW
            log(f'>CW cur={cur} diff={diff} cor={cor} left={FULL} right={FULL-abs(cor)}')
            motor2.throttle = FULL  # Left motor full
            motor1.throttle = FULL - abs(cor)  # Reduced                   
        time.sleep(0.25)  # 4 times a second
        hunds -= 1
    motor1.throttle = None
    motor2.throttle = None


def drive_cw_square(ofs,leg_time):    

    log('Going forward')
    turn_to(heading=ofs+0)
    drive_to(heading=ofs+0, secs=leg_time)

    log('Going right')
    turn_to(heading=ofs+90)
    drive_to(heading=ofs+90, secs=leg_time)

    log('Going backward')
    turn_to(heading=ofs+180)
    drive_to(heading=ofs+180, secs=leg_time)

    log('Going left')
    turn_to(heading=ofs+270)
    drive_to(heading=ofs+270, secs=leg_time)

LOGS = []
def log(message):
    LOGS.append(message)    

def write_log():
    with open('logs.txt','w') as f:
        for log in LOGS:
            f.write(log+'\n')


pixels[0] = (80,0,0) # Red LED ... we are moving
drive_cw_square(ofs=32,leg_time=3)
write_log()
pixels[0] = (0,80,0) # Green LED ... we are done

#while True:
#    print(get_current_heading())
#    time.sleep(0.5)

# for i in range(5):
#     motor1.throttle=0.5
#     motor2.throttle=0.5
#     time.sleep(2)
#     motor1.throttle=0
#     motor2.throttle=0
#     time.sleep(2)