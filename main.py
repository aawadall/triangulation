from building import Building
from fire_fighter import Firefighter
from beacon import Beacon
from plotter import Plotter


scale = [100, 100, 10]

building = Building(scale)
fireman_1 = Firefighter(bounds=scale)
beacons = [Beacon([-50, -50, 0], 'green'),
           Beacon([scale[0]/2, -50, 0], 'red'),
           Beacon([scale[0] + 50, -50, 0], 'green')
           ]

print("Fireman: ", fireman_1.name)
fireman_1.random_walk()
print("Location after random walk", fireman_1.location)

for _ in range(100):
    fireman_1.random_walk()

plotter = Plotter()

b_x, b_y, b_z = building.draw()
f_x, f_y, f_z = fireman_1.draw()

plotter.draw_line(f_x, f_y, f_z, color='green')
plotter.draw_line(b_x, b_y, b_z, color='black')

for beacon_1 in beacons:
    x, y, z = beacon_1.get_location()
    plotter.drw_scatter(x, y, z, beacon_1.color, beacon_1.marker)

plotter.show()
