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

plotter.draw_line(building.draw())
plotter.draw_line(fireman_1.draw())

for beacon_1 in beacons:
    plotter.drw_scatter(beacon_1.draw_beacon())

plotter.show()
