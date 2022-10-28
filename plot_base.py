# py -m pip install matplotlib

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

x0,y0,z0 = load_data('data/F_Base_no_power.json')
x1,y1,z1 = load_data('data/A_NoBase.json')

fig = plt.figure()
ax = plt.axes(projection='3d',xlabel='X',ylabel='Y',zlabel='Z',title='Robot Base Effects')

ax.scatter3D(0,0,0,c='black',s=100)
ax.scatter3D(x0,y0,z0,c='red',s=5)
ax.scatter3D(x1,y1,z1,c='blue',s=5)

plt.xlim([0,-70])
plt.ylim([0,-70])

plt.show()