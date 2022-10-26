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

x0,y0,z0 = load_data('data/A_NoBase.json')
x1,y1,z1 = load_data('data/B_NoBase_mounted_magnet.json')
x2,y2,z2 = load_data('data/C_NoBase_mounted_iron.json')

fig = plt.figure()
ax = plt.axes(projection='3d',xlabel='X',ylabel='Y',zlabel='Z',title='Mounted Effects')

ax.scatter3D(0,0,0,c='blue',s=100)
ax.scatter3D(x0,y0,z0,c='black',s=5)
ax.scatter3D(x1,y1,z1,c='red',s=5)
ax.scatter3D(x2,y2,z2,c='blue',s=5)

plt.show()