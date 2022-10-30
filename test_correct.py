import math

# Taken from "L_Base_no_power_north.json"
OFFSET_X = -34.500
OFFSET_Y = -41.591
SCALE_X = 0.9890
SCALE_Y = 1.0112

def correct(x,y):
    x = (x-OFFSET_X) * SCALE_X
    y = (y-OFFSET_Y) * SCALE_Y
    return (x,y)

def get_current_heading(mag_x,mag_y):
    #mag_x, mag_y, _ = sensor.magnetic
    ret = math.atan2(mag_x, mag_y)/math.pi*180
    return ret

from load_data import load_data

x,y,z = load_data('data/F_Base_no_power.json')
x,y,z = load_data('data/H_Base_100_forward.json')
x,y,z = load_data('data/L_Base_no_power_north.json')

for i in range(len(x)):
    a,b = correct(x[i],y[i])
    x[i] = a
    y[i] = b
    z[i] = 0

xmin = min(x)
xmax = max(x)
ymin = min(y)
ymax = max(y)

xc = xmin+(xmax-xmin)/2
yc = ymin+(ymax-ymin)/2

print(xmin,xmax,ymin,ymax,xc,yc)

print(get_current_heading(xc,yc))

import matplotlib.pyplot as plt

fig = plt.figure()
ax = plt.axes(projection='3d',xlabel='X',ylabel='Y',zlabel='Z')

ax.scatter3D(0,0,0,c='blue',s=100) # The origin
ax.scatter3D(x,y,z,c='blue',s=5) # The data
plt.xlim([-25,25])
plt.ylim([-25,25])

plt.show()