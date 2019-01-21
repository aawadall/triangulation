import random
import numpy as np
import scipy.optimize as op
import time
import matplotlib.pyplot as plt
import math
from mpl_toolkits.mplot3d import axes3d, Axes3D
from matplotlib import cm

# Initialize Data

x_scale = 500
y_scale = 300
z_scale = 150

scale = [x_scale, y_scale, z_scale]

noise = 3  # meters

# beacons
beacon_pos = []
distances = []

def draw_from_dist(distribution_range):
    return random.random() * distribution_range


def generate_random_point(_x_scale=x_scale,
                          _y_scale=y_scale,
                          _z_scale=z_scale):
    return [draw_from_dist(_x_scale),
            draw_from_dist(_y_scale),
            draw_from_dist(_z_scale)]


def bulk_distance(beacons, point):
    distance = []
    for beacon in beacons:

        d = (   (beacon[0] - point[0]) ** 2 +
                (beacon[1] - point[1]) ** 2 +
                (beacon[2] - point[2]) ** 2 +
                random.randrange(-1, 1) * noise) * \
                (1 + random.randrange(-1, 1) * 0.05)

        distance.append(max(d, 0))  # Make distance noise
                                    # a function of distance to simulate weak signal
    return np.sqrt(distance)


def single_point_distance(beacon, point):
    return np.sqrt((beacon[0] - point[0]) ** 2 +
                   (beacon[1] - point[1]) ** 2 +
                   (beacon[2] - point[2]) ** 2 +
                   random.randrange(-1, 1) * noise)

def non_lin_cost(x, beacons, distances):
    dist_hat = np.sqrt(np.sum(np.square(beacons - x), axis=1))
    return np.sqrt(np.square(distances - dist_hat))

def estimate_nonlin(beacons, distances):
    x_hat = generate_random_point()
    sol = op.least_squares(non_lin_cost, x_hat, verbose=0, args=(beacons, distances))
    return sol.x

# Ground truth point
_x = [0, 0, 0] #generate_random_point()

error = []
xy_loc = []
duration = []

x_motion = []
y_motion = []
z_motion = []

x_predict = []
y_predict = []
z_predict = []

velocity_vector = [0, 0, 0]
beta = 0.99

arm = 1

station_core_x = []
station_core_y = []
station_core_z = []
station_dims = [arm, arm, arm * 5]

# Station 1
station_core = [x_scale / 2, -50, 1]
station_core_x.append(station_core[0])
station_core_y.append(station_core[1])
station_core_z.append(station_core[2])
for x_idx in range(2):
    for y_idx in range(2):
        for z_idx in range(2):
            beacon_pos.append([station_core[0] + station_dims[0] * x_idx,
                               station_core[1] + station_dims[1] * y_idx,
                               station_core[2] + station_dims[2] * z_idx])

## # Beacons only
## station_core = [-50, -50, 1]
##
## y_idx = 0
## z_idx = 0
## for x_idx in range(x_scale, 0, -150):
##     for y_idx in range(-4, -3, 1):
##         for z_idx in range(4, 5, 1):
##             station_core = [-3 + x_idx, -3 + y_idx, z_idx + 0.1]
##             beacon_pos.append([station_core[0],
##                                station_core[1],
##                                station_core[2]])
##             station_core_x.append(station_core[0])
##             station_core_y.append(station_core[1])
##             station_core_z.append(station_core[2])







print("Running simulations")
for loc in range(1, 5000):
    print(loc)
    # beacons
    delta_v = [dx + random.randrange(-100, 100)/100 for dx in velocity_vector]
    for vidx in range(3):
        velocity_vector[vidx] = beta * velocity_vector[vidx] + (1-beta) * random.randrange(-100, 100)/10
        _x[vidx] += velocity_vector[vidx]
        # Geofencing
        if(_x[vidx] < 0):
            _x[vidx] = 0
        if(_x[vidx] > scale[vidx]):
            _x[vidx] = scale[vidx]

    if (loc % 500) == 0:  # place tracing beacon every 100 steps
        print('Add tracing beacon')
        station_core_x.append(_x[0]+1)
        station_core_y.append(_x[1]+1)
        station_core_z.append(_x[2]+1)
        beacon_pos.append([_x[0]+1, _x[1]+1, _x[2]+1])

    x_motion.append(_x[0])
    y_motion.append(_x[1])
    z_motion.append(_x[2])


    xy_loc.append(loc)


    distances = bulk_distance(beacon_pos, _x)

    start = time.time()
    solution = estimate_nonlin(beacon_pos, distances)
    end = time.time()

    x_predict.append(solution[0])
    y_predict.append(solution[1])
    z_predict.append(solution[2])

    e = single_point_distance(solution, _x)
    error.append(e)
    duration.append(1000 * (end - start))
    #time.sleep(1)

print("Finished Simulation")


fig = plt.figure()
ax = Axes3D(fig)

ax.plot3D(x_motion, y_motion, z_motion, c='green')

ax.scatter(x_predict, y_predict, z_predict, c=error, marker='o')
ax.scatter(station_core_x, station_core_y, station_core_z, marker='*',c='red')
ax.plot3D(station_core_x, station_core_y, station_core_z,c='black')
plt.show()
