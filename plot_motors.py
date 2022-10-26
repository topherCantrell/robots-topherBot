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
x1,y1,z1 = load_data('data/G_Base_50_forward.json')
x2,y2,z2 = load_data('data/H_Base_100_forward.json')
x3,y3,z3 = load_data('data/I_Base_50_backward.json')
x4,y4,z4 = load_data('data/J_Base_100_backward.json')

for i in range(len(z1)):
    z1[i] += 5
for i in range(len(z2)):
    z2[i] += 10
for i in range(len(z3)):
    z3[i] -= 5
for i in range(len(z4)):
    z4[i] -= 10

fig = plt.figure()
ax = plt.axes(projection='3d',xlabel='X',ylabel='Y',zlabel='Z',title='Motor Power')

ax.scatter3D(0,0,0,c='blue',s=100)

ax.scatter3D(x0,y0,z0,c='black',s=5)
ax.scatter3D(x1,y1,z1,c='yellow',s=5)
ax.scatter3D(x2,y2,z2,c='orange',s=5)
ax.scatter3D(x3,y3,z3,c='green',s=5)
ax.scatter3D(x4,y4,z4,c='blue',s=5)

plt.show()