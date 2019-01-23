from building import Building
from fire_fighter import Firefighter
from beacon import Beacon
from plotter import Plotter


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

plotter = Plotter()

b_x, b_y, b_z = building.draw()
f_x, f_y, f_z = fireman_1.draw()

plotter.draw_line(f_x, f_y, f_z, color='green')
plotter.draw_line(b_x, b_y, b_z, color='black')

plotter.show()
