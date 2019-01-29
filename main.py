from building import Building
from fire_fighter import Firefighter
from beacon import Beacon
from plotter import Plotter


scale = [100, 100, 10]

building = Building(scale)
firemen = []

for f in range(10):
    firemen.append(Firefighter(bounds=scale, max_v=f/10))
beacons = [Beacon([-50, -50, 0], 'green'),
           Beacon([scale[0]/2, -50, 0], 'red'),
           Beacon([scale[0] + 50, -50, 0], 'green')
           ]

for _ in range(1000):
    for fireman_1 in firemen:
        fireman_1.random_walk()


plotter = Plotter()

plotter.draw_line(building.draw())

for fireman_1 in firemen:
    plotter.draw_line(fireman_1.draw())

for beacon_1 in beacons:
    plotter.drw_scatter(beacon_1.draw_beacon())

plotter.show()
