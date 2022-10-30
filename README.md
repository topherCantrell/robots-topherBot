# robots-compass-bot

Experiments with a Compass Module

![](art/CompassBot5.jpg)

![](art/CompassBot3.jpg)

## Hardware

### Two wheel robot base ($13)
https://www.amazon.com/dp/B01LXY7CM3

![](art/chassis.jpg)

### Robot control board ($15)
https://www.adafruit.com/product/5129

![](art/pico.jpg)

https://github.com/CytronTechnologies/MAKER-PI-RP2040

Writeable filesystem:

https://learn.adafruit.com/circuitpython-essentials/circuitpython-storage

### Compass module LSM303DLHC ($8)
https://www.amazon.com/HiLetgo-LSM303DLHC-Compass-Accelerometer-Magnetometer/dp/B07X3GFKYD

![](art/compass.jpg)

```
>>> import machine
>>> i2c = machine.I2C(scl=machine.Pin(5), sda=machine.Pin(4))
>>> i2c.scan()
[25, 30]
>>>
```

!(https://www.st.com/resource/en/datasheet/lsm303dlhc.pdf)[https://www.st.com/resource/en/datasheet/lsm303dlhc.pdf]

![](art/maglibs.jpg)

Hex 19: 00011001 (Linear acceleration)

Hex 1E: 00011110 (Compass)

https://github.com/adafruit/Adafruit_CircuitPython_LSM303DLH_Mag

## Other Hardware Options

### More grove connector wires ($3.50 for 5)
https://www.seeedstudio.com/Grove-4-pin-Female-Jumper-to-Grove-4-pin-Conversion-Cable-5-PCs-per-PAck.html

![](art/grove.jpg)

### Raspberry Pi motor hat (can be used as generic I2C motor driver without a pi) ($18)
https://www.amazon.com/dp/B098B1P8BS 

The power switch: connects the VIN terminals to the board. The "OFF" position connects VIN, the "ON" position does not. Seems backwards. Might be related to getting power from the pi instead.

The edge of the board has header holes for:
  * 5V connects to the board's 5V regulator output to the raspberry pi's 5V pin
  * 3.3V does NOT connect to the raspberry pi's 3V pin since the Pi drives this
  * GND connects to common ground on board and pi
  * SCL and SDA connect to PI pins 

With the ESP8266. D1 wired to SCL, D2 wired to SDA. An I2C scan reboots the ESP. Other devices scan correctly from the ESP. Very odd. 

Trying from the Pi: i2cdetect shows addresses 40 and 70. Seems to work from the pi.

![](art/hat.jpg)

### ESP8266 ($16 for five)
https://www.amazon.com/dp/B073CQVFLK 

![](art/esp8266.jpg)

### Wheel encoder readers (for future projects) ($9 for the pair)
https://www.amazon.com/dp/B00EERJDY4 

![](art/encoders.jpg)

## 3D point plotter

```

# py -m pip install matplotlib

import json
with open('data.txt') as f:
    data = json.load(f)

import matplotlib.pyplot as plt
fig = plt.figure()
ax = plt.axes(projection='3d',xlabel='X',ylabel='Y',zlabel='Z',title='Compass Spin')

ax.scatter3D(0,0,0,c='blue',s=100)

plt.show()
```

## Graphs

These graphs were made by spinning the compass module in a circle about the gravity vector. The Z axis of
the compass is parallel to gravity. The (x, y) plane is parallel to the Earth.

### With and without motors
Made with `plot_base.py`.

The motors have magnets (and iron) in them. How do the motors affect the compass reading? Let's spin the
compass/controller/batteries with and without the robot base attached.

![](art/plot_base.jpg)

Interestingly, the motors bend the readings closer to ideal (zero slope in Z).

### Magnet and iron mounted to robot
Made with `plot_mounted.py`.

How does a magnet attached to the robot affect the compass readings? How does a chunk of iron attached to
the robot affect the compass readings? Let's spin compass/controller/batteries with iron attached.

![](art/plot_mounted.jpg)

With no magnet and no iron, the readings (black curve) are offset from center. This is caused by hard and soft
iron built into the compass/controller/batteries. Mounting screws and header pins contribute to this offset.

The magnet pushes the readings (red curve) away from the origin. The iron (blue curve) does too, but less noticeably.

### Magnet and iron external to robot
Made with `plot_externals.py`.

How does a magnet placed near the robot (but not attached) affect the compass readings? How does a chunk of iron
placed near the robot (but not attached) affect the compass readings?

![](art/plot_externals.jpg)

The iron I used is a square tube stood upright along the Z axis. Notice how the blue curve is distorted along the Z axis.

The magnet wreaks havoc with the readings (red curve).

### Running motors
Made with `plot_motors.py`.

When a motor is running, the current creates an electromagnet within each motor. Does this affect the compass readings?

Let's run the motors at full and half power both backwards and forwards.

![](art/plot_motors.jpg)

The Z-axises of these curves have been tweaked to separate the curves visually. Just looking at the (x, y) values we find that
all of the curves are nearly identical. The readings are affected the same whether the motors are running or not.

### Calibration
Made with `calibrate.py`

The Z slope is slight. We will ignore the compass readings on the Z axis. The (x, y) offsets are easy to calculate and adjust for.
The distortion, or squashing, of the circle by soft-iron is harder to correct for. We'll use the "simple" correction factor because
it is computationally cheap.

![](art/plot_calibrate.jpg)

Notice that the final (black) curve is not a perfect circle. The "simple" correction algorithm leaves a little error, but it is close
enough to perfect for our use.