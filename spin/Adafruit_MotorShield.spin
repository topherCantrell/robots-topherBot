{{

Default I2C address:      0x40
  
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

' Adjust these for whatever I2C driver you want to use
OBJ
  i2c  : "Basic_I2C_Driver_1.spin"
pri read8(addr)  
  i2c.ReadByte (pin_scl, i2caddr, addr | i2c#OneAddr) 
pri write8(addr,value)
  i2c.WriteByte(pin_scl, i2caddr, addr | i2c#OneAddr, value)
pri writeMulti(addr, buffer, count)
  i2c.WritePage(pin_scl, i2cAddr, addr | i2c#OneAddr, buffer, count)
    
VAR
  byte pin_scl
  byte i2caddr
  byte setPWMData[4]
  
PUB init(addr)  
  i2caddr := addr

PUB begin(scl) ' SDA = SCL + 1
  pin_scl := scl   
  i2c.Initialize(scl)
  reset

PUB reset
  write8(PCA9685_MODE1, $00)

PUB setPWMFreq(freq) | oldmode, newmode, prescale
  ' TODO calculate prescale
  oldmode := read8(PCA9685_MODE1)
  newmode := (oldmode & $7F) | $10     ' sleep
  write8(PCA9685_MODE1, newmode)       ' go to sleep
  write8(PCA9685_PRESCALE, prescale)   ' set the prescaler
  write8(PCA9685_MODE1, oldmode)
  PauseMSec(5)
  write8(PCA9685_MODE1, oldmode | $A1) ' set MOD1 register to turn on auto increment    

PUB setPWM(num, on, off)   
  setPWMData[0] := on
  setPWMData[1] := on >> 8
  setPWMData[2] := off
  setPWMData[3] := off >> 8
  writeMulti(LED0_ON_L+4*num, @setPWMData,4)  

pri PauseMSec(Duration)
  waitcnt(((clkfreq / 1_000 * Duration - 3932) #> 381) + cnt)