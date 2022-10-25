# micropython implementation

import machine
i2c = machine.I2C(scl=machine.Pin(5), sda=machine.Pin(4))


def configure_compass():
    # The compass module only has 3 writeable registers. The first
    # register (00) configures the temperature sensor and data rate. The
    # second reigister (01) configures the sensor input field range.
    # The third (02) configures the operating mode.

    # The default configuration for 00 and 01 is fine:
    #
    #            T xx DDD xx
    # CRA_REG_M [0_00_100_00]  Temperature off, data rate 15Hz
    #
    #            GGG xxxxx
    # CRB_REG_M [001_00000]    Sensor input filed range +/- 1.3gauss

    # Now to bring the chip out of sleep mode and start continuous conversion

    i2c.writeto_mem(0x1E, 2, b'\x00')


def get_compass():
    # Wait on the DRDY bit in the SR_REG_M to signal new data is ready
    while True:
        g = i2c.readfrom_mem(0x1E, 9, 1)
        if g[0] & 1:
            g = i2c.readfrom_mem(0x1E, 3, 6)
            x = (g[0] << 8) | g[1]
            if x > 0x7FFF:
                x -= 0x10000
            z = (g[2] << 8) | g[3]
            if z > 0x7FFF:
                z -= 0x10000
            y = (g[4] << 8) | g[5]
            if y > 0x7FFF:
                y -= 0x10000
            # Scaling factors from the datasheet for +/- 1.3 gauss
            return (x/1100, y/1100, z/980)
