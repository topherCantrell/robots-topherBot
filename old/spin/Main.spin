CON
  _clkmode        = xtal1 + pll16x
  _xinfreq        = 5_000_000 

PIN_NEO = 26

PIN_MOTOR_SCL = 8
'PIN_MOTOR_SDA = 9

'PIN_LINE_SCL = 10
'PIN_LINE_SDA = 11

'PIN_ENC_LEFT  = 16
'PIN_END_RIGHT = 17

'PIN_PI_TX = -1
'PIN_PI_RX = -1



OBJ
    'MOTORS : "Adafruit_MotorShield"
    PST    : "Parallax Serial Terminal"
    STRIP  : "NeoPixelStrip"

    i2c  : "Basic_I2C_Driver_1.spin" 

PUB Main | a

PauseMSec(2_000) 

  PST.start(115200)

  PST.str(string("MOTORS",13))


  i2c.Initialize(PIN_MOTOR_SCL)

  a := i2c.ReadByte (PIN_MOTOR_SCL, $60, 0 | i2c#OneAddr)

  PST.hex(a,4)  


  'MOTORS.init($60,PIN_MOTOR_SCL)
  'PauseMSec(1000)
  
  'MOTORS.setPWM(8,  0, 200)
  'MOTORS.setPWM(9,  4096, 0)
  'MOTORS.setPWM(10, 0, 4096)  

  

  '
  
  'PauseMSec(2_000)

  'i2c.Start(PIN_SCL)
  'i2c.Write(PIN_SCL,0x60)
  'i2c.Write(PIN_SCL,rate)
  'i2c.Stop(PIN_SCL)

  dira[PIN_NEO] := 1
  outa[PIN_NEO] := 0

  STRIP.init
  STRIP.draw(2, @colors, @pixelPattern, PIN_NEO, 20)

  repeat       

PRI PauseMSec(Duration)
  waitcnt(((clkfreq / 1_000 * Duration - 3932) #> 381) + cnt)

DAT

colors
    long $00_00_00_00
    long $00_00_00_10
    long $00_00_10_00
    long $00_10_00_00
    long $00_10_10_10

pixelPattern
    byte 1,2, 3,3,3,4,3,3,3,4,  4,3,3,3,3,3,3,3,1,1
    