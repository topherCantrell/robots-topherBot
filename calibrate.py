import json

import matplotlib.pyplot as plt

def load_data(fname):

    with open(fname) as f:
        data = json.load(f)

    xdata = []
    ydata = []
    zdata = []
    for x,y,z in data:
        xdata.append(x)
        ydata.append(y)
        zdata.append(z)

    return xdata,ydata,zdata

fname = 'data/M_Base_mounted_iron.json'
#x,y,z = load_data('data/F_Base_no_power.json')
x,y,z = load_data(fname)
x1,y1,z1 = load_data(fname)
x2,y2,z2 = load_data(fname)

xmax = max(x)
xmin = min(x)
xavg = (xmax - xmin)/2
xoffset = xmax - xavg
#print('xmax/min:',xmax,xmin,xmax-xmin)

ymax = max(y)
ymin = min(y)
yavg = (ymax - ymin)/2
yoffset = ymax - yavg

avgdelta = (xavg+yavg)/2
xscale = avgdelta / xavg
yscale = avgdelta / yavg
#print('ymax/min:',ymax,ymin,ymax-ymin)

print(xoffset,yoffset)
print(xscale,yscale)

for i in range(len(x)):
    x[i] = (x[i]-xoffset) * xscale
    x1[i] = x1[i]-xoffset

for i in range(len(y)):
    y[i] = (y[i]-yoffset) * yscale
    y1[i] = (y1[i]-yoffset)

for i in range(len(z)):
    z[i] = 0
    z1[i] = 0

fig = plt.figure(figsize=(8,8))

"""
ax = plt.axes(projection='3d',xlabel='X',ylabel='Y',zlabel='Z')
ax.scatter3D(0,0,0,c='black',s=100) # Origin
#
ax.scatter3D(x,y,z,c='black',s=5)
ax.scatter3D(x1,y1,z1,c='blue',s=5)
ax.scatter3D(x2,y2,z2,c='red',s=5)
"""

ax = plt.axes(xlabel='X',ylabel='Y')
ax.scatter(0,0,c='black',s=100)
ax.scatter(x,y,c='black',s=5)
ax.scatter(x1,y1,c='blue',s=5)
#ax.scatter(x2,y2,c='red',s=5)

plt.xlim([-40,40])
plt.ylim([-40,40])

plt.show()