import smbus
import time

bus = smbus.SMBus(1)
address = 0x60

bus.write_byte_data(address,0,1)      # ALLCALL enabled (optional)
time.sleep(0.005)                     # Wait for oscillator

def set_pwm_freq(freq):
    # TODO. Remember to set the SLEEP bit before you change the PRESCALER.
    # Then remember to set it back. At startup the, PRESCALER is 0x1E (200Hz).
    # The maximum frequency is PRESCALER=3 (1526Hz)
    pass

def set_pwm(channel, on_cnt, off_cnt):
    # Each channel has 4 registers (a word for ON time and a word for OFF time)
    bus.write_byte_data(address, 6+channel*4,  on_cnt & 0xFF)
    bus.write_byte_data(address, 7+channel*4,  on_cnt >> 8)
    bus.write_byte_data(address, 8+channel*4, off_cnt & 0xFF)
    bus.write_byte_data(address, 9+channel*4, off_cnt >> 8)

def set_bool(channel, value):
    # Set the output pin to a solid value -- 1 or 0
    if value:
        set_pwm(channel,4096,0)
    else:
        set_pwm(channel,0,4096)
        
# This maps output channels to motors. There are 3 channels per motor.
# The first channel is the motor's PWM.
# The second and third channels are the boolean directions.
MOTORS = (
    (8,9,10),   # Front right: FALSE+TRUE = forward
    (13,12,11), # Back right:  TRUE+FALSE = forward
    (2,3,4),    # Back left:   TRUE+FALSE = forward
    (7,6,5)     # Front left:  FALSE+TRUE = forward
)

def set_motors(left_speed, right_speed):
    
    """set the speeds of the left/right side motors
    
    The motors on each side always turn in the same direction.
    Positive speeds are forwards.
    Negative speeds are backwards.
    A speed of None will release the motor current.
    
    """
    
    # This is all brute force ... just for demo
        
    if right_speed == None:
        # Release both motors
        set_pwm(MOTORS[0][0],0,0)
        set_bool(MOTORS[0][1],False)
        set_bool(MOTORS[0][2],False)
        set_pwm(MOTORS[1][0],0)
        set_bool(MOTORS[1][1],False)
        set_bool(MOTORS[1][2],False)        
    else:
        # Backwards or forwards
        if right_speed<0:            
            set_pwm(MOTORS[0][0],0,-right_speed)
            set_bool(MOTORS[0][2],False)
            set_bool(MOTORS[0][1],True)                        
            set_pwm(MOTORS[1][0],0,-right_speed)
            set_bool(MOTORS[1][1],False)
            set_bool(MOTORS[1][2],True) 
                        
        else:
            set_pwm(MOTORS[0][0],0,right_speed)
            set_bool(MOTORS[0][1],False)
            set_bool(MOTORS[0][2],True)            
            set_pwm(MOTORS[1][0],0,right_speed)
            set_bool(MOTORS[1][2],False) 
            set_bool(MOTORS[1][1],True)              
           
    if left_speed == None:
        # Release both motors
        set_pwm(MOTORS[2][0],0,0)
        set_bool(MOTORS[2][1],False)
        set_bool(MOTORS[2][2],False)
        set_pwm(MOTORS[3][0],0)
        set_bool(MOTORS[3][1],False)
        set_bool(MOTORS[3][2],False)        
    else:
        # Backwards or forwards
        if left_speed<0:            
            set_pwm(MOTORS[2][0],0,-left_speed)
            set_bool(MOTORS[2][1],False)
            set_bool(MOTORS[2][2],True)            
            set_pwm(MOTORS[3][0],0,-left_speed)
            set_bool(MOTORS[3][2],False) 
            set_bool(MOTORS[3][1],True)            
        else:
            set_pwm(MOTORS[2][0],0,left_speed)
            set_bool(MOTORS[2][2],False)
            set_bool(MOTORS[2][1],True)
            set_pwm(MOTORS[3][0],0,left_speed)
            set_bool(MOTORS[3][1],False)              
            set_bool(MOTORS[3][2],True)                       


# Drive a square (times calibrated for my carpet)

set_motors(1000,1000)
time.sleep(2)
set_motors(1000,-1000)
time.sleep(1.3)
set_motors(1000,1000)
time.sleep(2)
set_motors(1000,-1000)
time.sleep(1.3)
set_motors(1000,1000)
time.sleep(2)
set_motors(1000,-1000)
time.sleep(1.3)
set_motors(1000,1000)
time.sleep(2)
set_motors(1000,-1000)
time.sleep(1.3)

set_motors(0,0)
