from building import Building
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d, Axes3D

scale = [10, 10, 10]

building = Building(scale)

fig = plt.figure()
b_fig = building.draw(fig)

plt.show()
