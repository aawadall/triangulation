from building import Building
from fire_fighter import Firefighter
from beacon import Beacon
import matplotlib.pyplot as plt

from mpl_toolkits.mplot3d import axes3d, Axes3D

scale = [10, 10, 10]

building = Building(scale)
fireman_1 = Firefighter(bounds=scale)
beacon_1 = Beacon([0, 0, 0])

print("Fireman: ", fireman_1.name)
fireman_1.random_walk()
print("Location after random walk", fireman_1.location)

for _ in range(100):
    fireman_1.random_walk()
print("Beacon: ", beacon_1.name, "location: ", beacon_1.location)
fig = plt.figure()

f_fig = fireman_1.draw(fig)
b_fig = building.draw(fig)

f_fig.draw()
plt.show()

