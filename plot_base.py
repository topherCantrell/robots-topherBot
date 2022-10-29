# py -m pip install matplotlib

import matplotlib.pyplot as plt

from load_data import load_data

x0,y0,z0 = load_data('data/F_Base_no_power.json')
x1,y1,z1 = load_data('data/A_NoBase.json')

fig = plt.figure(figsize=(9,8))
# ax = plt.axes(projection='3d',xlabel='X',ylabel='Y',zlabel='Z',title='Robot Base Effects')
ax = plt.axes(projection='3d',xlabel='X',ylabel='Y',zlabel='Z')

ax.scatter3D(0,0,0,c='black',s=100) # Origin
#
ax.scatter3D(x0,y0,z0,c='red',s=5)
ax.scatter3D(x1,y1,z1,c='blue',s=5)

plt.xlim([0,-80])
plt.ylim([0,-80])

#ax.view_init(elev=29, azim=-171, roll=0) # 3D view
ax.view_init(elev=90, azim=0, roll=0) # Just X,Y (no Z)
#ax.view_init(elev=0, azim=-90, roll=0) # Just X,Z (shows the Z changes)

plt.show()