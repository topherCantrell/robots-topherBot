# py -m pip install matplotlib

import json
import matplotlib.pyplot as plt

#fname = 'data/A_NoBase.json'
#fname = 'data/B_NoBase_mounted_magnet.json'
#fname = 'data/C_NoBase_mounted_iron.json'
#fname = 'data/D_NoBase_50_magnet.json'
#fname = 'data/E_NoBase_50_iron.json'
#fname = 'data/F_Base_no_power.json'
#fname = 'data/G_Base_50_forward.json'
#fname = 'data/H_Base_100_forward.json'
#fname = 'data/I_Base_50_backward.json'
#fname = 'data/J_Base_100_backward.json'
#fname = 'data/K_Base_L100forward_R100backward.json'
#fname = 'data/L_Base_no_power_north.json'

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

x1,y1,z1 = load_data('data/F_Base_no_power.json')
x2,y2,z2 = load_data('data/H_Base_100_forward.json')
for i in range(len(z2)):
    z2[i] -= 10
x3,y3,z3 = load_data('data/J_Base_100_backward.json')
for i in range(len(z3)):
    z3[i] += 10

fig = plt.figure()
ax = plt.axes(projection='3d',xlabel='X',ylabel='Y',zlabel='Z',title='Compass Spin')

ax.scatter3D(0,0,0,c='blue',s=100)

ax.scatter3D(x1,y1,z1,c='green',s=5)
ax.scatter3D(x2,y2,z2,c='red',s=5)
ax.scatter3D(x3,y3,z3,c='yellow',s=5)

plt.show()