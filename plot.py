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
fname = 'G:\data.txt'

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

"""
x0,y0,z0 = load_data('data/F_Base_no_power.json')
x1,y1,z1 = load_data('data/G_Base_50_forward.json')
x2,y2,z2 = load_data('data/H_Base_100_forward.json')
x3,y3,z3 = load_data('data/I_Base_50_backward.json')
x4,y4,z4 = load_data('data/J_Base_100_backward.json')
x5,y5,z5 = load_data('data/A_NoBase.json')

for i in range(len(z1)):
    z1[i] += 5
for i in range(len(z2)):
    z2[i] += 10
for i in range(len(z3)):
    z3[i] -= 5
for i in range(len(z4)):
    z4[i] -= 10
for i in range(len(z5)):
    z5[i] -= 20
    """

fig = plt.figure()
ax = plt.axes(projection='3d',xlabel='X',ylabel='Y',zlabel='Z',title='Compass Spin')

ax.scatter3D(0,0,0,c='blue',s=100)

# ax.scatter3D(x0,y0,z0,c='black',s=5)
# ax.scatter3D(x1,y1,z1,c='yellow',s=5)
# ax.scatter3D(x2,y2,z2,c='orange',s=5)
# ax.scatter3D(x3,y3,z3,c='green',s=5)
# ax.scatter3D(x4,y4,z4,c='blue',s=5)
# ax.scatter3D(x5,y5,z5,c='red',s=5)

#x0,y0,z0 = load_data('data/E_NoBase_50_iron.json')
#x0,y0,z0 = load_data('data/D_NoBase_50_magnet.json')
#x0,y0,z0 = load_data('data/F_Base_no_power.json')

x0,y0,z0 = load_data(fname)
ax.scatter3D(x0,y0,z0,c='red',s=5)

plt.show()