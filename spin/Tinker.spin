CON
  _clkmode        = xtal1 + pll16x
  _xinfreq        = 5_000_000 

  PIN_SCL    = 0
  'PIN_DAT   = 1

OBJ
    i2c  : "Basic_I2C_Driver_1.spin"
    PST  : "Parallax Serial Terminal" 


pri PauseMSec(Duration)
  waitcnt(((clkfreq / 1_000 * Duration - 3932) #> 381) + cnt)
      
PUB Main | fn, param, retVal

  i2c.Initialize(PIN_SCL)
  
  PauseMSec(2_000)

  i2c.Start(PIN_SCL)
  i2c.Write(PIN_SCL,0x60)
  i2c.Write(PIN_SCL,rate)
  i2c.Stop(PIN_SCL) 