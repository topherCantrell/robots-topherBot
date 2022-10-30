# py -m pip install matplotlib
import matplotlib.pyplot as plt
from load_data import load_data

#x,y,z = load_data('data.json')
x,y,z = load_data('data/L_Base_no_power_north.json')

fig = plt.figure()
ax = plt.axes(projection='3d',xlabel='X',ylabel='Y',zlabel='Z')

ax.scatter3D(0,0,0,c='blue',s=100) # The origin
ax.scatter3D(x,y,z,c='blue',s=5) # The data

plt.show()