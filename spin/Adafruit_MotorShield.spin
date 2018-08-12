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
'pri writeMulti(addr, buffer, count)
'  i2c.WritePage(pin_scl, i2cAddr, addr | i2c#OneAddr, buffer, count)
    
VAR
  byte pin_scl
  byte i2caddr
  'byte setPWMData[4]
  
PUB init(addr,scl)  
  i2caddr := addr
  pin_scl := scl ' SDA = SCL + 1 
  i2c.Initialize(scl)
  PauseMSec(1000)
  write8(PCA9685_MODE1,$1)
  PauseMSec(1000) 

PUB setBOOL(num, onOff)
  if onOff==1
    setPWM(num,4096,0)
  else
    setPWM(num,0,4096)

PUB setPWM(num, on, off)

  write8(LED0_ON_L +4*num, on & $FF)
  write8(LED0_ON_H +4*num, (on >> 8) & $FF)
  write8(LED0_OFF_L+4*num, off & $FF)
  write8(LED0_OFF_H+4*num, (off >> 8) & $FF)     

  'setPWMData[0] := on
  'setPWMData[1] := on >> 8
  'setPWMData[2] := off
  'setPWMData[3] := off >> 8
  'writeMulti(LED0_ON_L+4*num, @setPWMData,4)  

pri PauseMSec(Duration)
  waitcnt(((clkfreq / 1_000 * Duration - 3932) #> 381) + cnt)