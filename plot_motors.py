# py -m pip install matplotlib

import matplotlib.pyplot as plt

from load_data import load_data

x0,y0,z0 = load_data('data/F_Base_no_power.json')
x1,y1,z1 = load_data('data/G_Base_50_forward.json')
x2,y2,z2 = load_data('data/H_Base_100_forward.json')
x3,y3,z3 = load_data('data/I_Base_50_backward.json')
x4,y4,z4 = load_data('data/J_Base_100_backward.json')

# Offset them in Z to visually separate them
for i in range(len(z1)):
    z1[i] += 5
for i in range(len(z2)):
    z2[i] += 10
for i in range(len(z3)):
    z3[i] -= 5
for i in range(len(z4)):
    z4[i] -= 10

fig = plt.figure(figsize=(9,8))
ax = plt.axes(projection='3d',xlabel='X',ylabel='Y',zlabel='Z')

ax.scatter3D(0,0,0,c='black',s=100) # Origin
#
ax.scatter3D(x0,y0,z0,c='black',s=5)
ax.scatter3D(x1,y1,z1,c='yellow',s=5)
ax.scatter3D(x2,y2,z2,c='orange',s=5)
ax.scatter3D(x3,y3,z3,c='green',s=5)
ax.scatter3D(x4,y4,z4,c='blue',s=5)

plt.show()