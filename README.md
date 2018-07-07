# Topher Bot

I added a 20-pixel neopixel strip to the front of the car for a K.I.T.T. (Knight Rider) effect.

TODO Next:
  - I'm not sure I need two spin files for the single board. Simplify.
  - Add some code in Main.spin to move the wheels.

## Links

MotorShield v2.3
  - [http://adafruit.com/products/1438](http://adafruit.com/products/1438)

Driver manual
  - [https://cdn-shop.adafruit.com/datasheets/PCA9685.pdf](https://cdn-shop.adafruit.com/datasheets/PCA9685.pdf)

Shield schematics
  - [https://learn.adafruit.com/assets/34460](https://learn.adafruit.com/assets/34460)

Wheel Encoder
  - http://www.tinyosshop.com/index.php?route=product/product&filter_name=wheel%20encoder&filter_description=true&product_id=541

Line Follower
  - https://github.com/sparkfun/Line_Follower_Array

Parallax quick start
  - https://www.parallax.com/sites/default/files/downloads/40000-Propeller-QuickStart-Schematic-Layout-RevB.pdf
  
5V/3.3V Converter (BOB)
  - https://www.sparkfun.com/products/12009

## Hardware: Pi + MotorController

You can run the motor controller right off the PiZero -- no propeller board needed. The wiring looks
like this:

![](https://github.com/topherCantrell/robots-topherBot/blob/master/art/piOnly.jpg)

Remember to make the solder jumper on the shield for 3.3V power input.

The `python` folder has the `py_only.py` code. There are no frills in the code. I wanted to
keep it as minimal as possible.

## Hardware: Everything

Adafruit motor controller shield mounted to base. Line follower array mounted to front.

![](https://github.com/topherCantrell/robots-topherBot/blob/master/art/bottom.jpg)

Encoder reader mounted on top:

![](https://github.com/topherCantrell/robots-topherBot/blob/master/art/cover.jpg)

Before wiring:

![](https://github.com/topherCantrell/robots-topherBot/blob/master/art/bare.jpg)

Schematic:

![](https://github.com/topherCantrell/robots-topherBot/blob/master/art/schematic.jpg)

## Tests

```
i2cdetect -y 1
```

Shows 60 and 70. 70 is the "all call" (useful if the driver is running many LED boards).



