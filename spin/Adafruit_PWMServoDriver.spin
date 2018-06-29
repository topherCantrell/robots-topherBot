{{

Default I2C address:      0x60
Default begin frequency:  1600

Motor PWM  IN2 IN1
 M1   8    9   10
 M2   13   12  11
 M3   2    3   4
 M4   7    6   5

Stepper PWMA PWMB AIN1 AIN2 BIN1 BIN2
 S1     8     13   10   9    11   12
 S2     2     7    4    3    5     6  
 
}}

CON

PCA9685_SUBADR1 = $02
PCA9685_SUBADR2 = $03
PCA9685_SUBADR3 = $04

PCA9685_MODE1 = $00
PCA9685_PRESCALE = $FE

LED0_ON_L = $06
LED0_ON_H = $07
LED0_OFF_L = $08
LED0_OFF_H = $09

ALLLED_ON_L = $FA
ALLLED_ON_H = $FB
ALLLED_OFF_L = $FC
ALLLED_OFF_H = $FD

PUB init(addr)

PUB begin

PUB reset

PUB setPWMFreq(freq)

PUB setPWM(num, on, off)

pri read8(addr)

pri write8(addr,value)