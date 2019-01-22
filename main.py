from building import Building
from fire_fighter import Firefighter
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d, Axes3D

scale = [10, 10, 10]

building = Building(scale)
fireman_1 = Firefighter(bounds=scale)

print(fireman_1.name)
fireman_1.random_walk()
print(fireman_1.location)
fig = plt.figure()
b_fig = building.draw(fig)

plt.show()

