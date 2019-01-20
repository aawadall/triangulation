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

noise = 4  # meters

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
        distance.append((beacon[0] - point[0]) ** 2 +
                        (beacon[1] - point[1]) ** 2 +
                        (beacon[2] - point[2]) ** 2 +
                        random.randrange(-1, 1) * noise)
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
    solution = op.least_squares(non_lin_cost,  x_hat, verbose=0,args=(beacon_pos, distances))
    return solution.x

# Ground truth point
_x = generate_random_point()

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
beta = 0.999

arm = 1.3
station_dims = [arm, arm, arm]
# Station 1
station_core = [-50, -50, 1]

for x_idx in range(2):
    for y_idx in range(2):
        for z_idx in range(2):
            beacon_pos.append([station_core[0] + station_dims[0] * x_idx,
                               station_core[1] + station_dims[1] * y_idx,
                               station_core[2] + station_dims[2] * z_idx])

# Station 2
station_core = [x_scale/2, -50, 1]

for x_idx in range(2):
    for y_idx in range(2):
        for z_idx in range(2):
            beacon_pos.append([station_core[0] + station_dims[0] * x_idx,
                               station_core[1] + station_dims[1] * y_idx,
                               station_core[2] + station_dims[2] * z_idx])

# Station 3
station_core = [x_scale + 50, -50, 1]

for x_idx in range(2):
    for y_idx in range(2):
        for z_idx in range(2):
            beacon_pos.append([station_core[0] + station_dims[0] * x_idx,
                               station_core[1] + station_dims[1] * y_idx,
                               station_core[2] + station_dims[2] * z_idx])


print("Running simulations")
for loc in range(0, 500):
    print(loc)
    # beacons
    delta_v = [dx + random.randrange(-100, 100)/100 for dx in velocity_vector]
    for vidx in range(3):
        velocity_vector[vidx] = beta * velocity_vector[vidx] + (1-beta) * random.randrange(-100, 100)/1000
        _x[vidx] += velocity_vector[vidx]

    x_motion.append(_x[0])
    y_motion.append(_x[1])
    z_motion.append(_x[2])

    arm = 2.2
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
#print(error)
#print(xy_loc)

fig = plt.figure()
ax = Axes3D(fig)
#ax = fig.add_subplot(111, projection='3d')
ax.plot3D(x_motion, y_motion, z_motion, c='gray')
#ax.scatter(x_motion, y_motion, z_motion, c='green', marker='^')
ax.plot3D(x_predict, y_predict, z_predict, linestyle=':')
ax.scatter(x_predict, y_predict, z_predict, c=duration, marker='o')
#ax.scatter(station_core[0], station_core[1], station_core[2], marker='*')
#ax.annotate('Station',(station_core[0], station_core[1]))
plt.show()
