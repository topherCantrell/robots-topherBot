# This becomes "boot.py" on the CircuitPython drive.

# At boot we look at button GP21. If it is held down, then
# the filesystem is writeable by the program but not PC. This
# code beeps to confirm that state.
# 
# If it is not held down, then the filesystem is writeable by PC
# but not the program.
#
# The front Neo is red if the PC is read-only. The front Neo is
# green if the PC can write.

import board
import neopixel
import digitalio
import storage
import simpleio
import time

PIEZO_PIN = board.GP22

pixels = neopixel.NeoPixel(board.GP18,2) # 2 pixels. we use the [0]
pixels.fill(0)

btn21 = digitalio.DigitalInOut(board.GP21)
btn21.direction = digitalio.Direction.INPUT
btn21.pull = digitalio.Pull.UP

if btn21.value:
    # NOT PRESSED
    # Filesystem is writeable by PC (not program)
    pixels[0] = (0,80,0)
    storage.remount("/", readonly=True)
else:
    # PRESSED
    # Filesystem is writeable by program (not PC)
    pixels[0] = (80,0,0)
    storage.remount("/", readonly=False)
    simpleio.tone(PIEZO_PIN, 262, duration=0.1)
    simpleio.tone(PIEZO_PIN, 659, duration=0.15)
    simpleio.tone(PIEZO_PIN, 784, duration=0.2)

time.sleep(1)