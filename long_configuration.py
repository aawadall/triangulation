import random
import numpy as np
import scipy.optimize as op
import time
import matplotlib.pyplot as plt
import math
# Initialize Data

x_scale = 500
y_scale = 300
z_scale = 150

scale = [x_scale, y_scale, z_scale]

noise = 7  # meters

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

print("Running simulations")
for loc in range(0, 300):
    print(loc)
    # beacons

    x_inc = [x_el + random.randrange(-100,100)/100 for x_el in _x]
    _x = x_inc
    x_motion.append(_x[0])
    y_motion.append(_x[1])
    z_motion.append(_x[2])

    arm = 2.2
    xy_loc.append(loc)

    station_dims = [arm, arm, arm]
    # Station 1
    station_core = [-150, -20 , 1]
    #beacon_pos.append([station_core[0] + 0,
    #                   station_core[1] + 0,
    #                   station_core[2] + 0])
    #beacon_pos.append([station_core[0] + station_dims[0],
    #                   station_core[1] + 0,
    #                   station_core[2] + 0])
    #beacon_pos.append([station_core[0] + 0,
    #                   station_core[1] + station_dims[1],
    #                   station_core[2] + 0])
    #beacon_pos.append([station_core[0] + station_dims[0],
    #                   station_core[1] + station_dims[1],
    #                   station_core[2] + 0])
    #beacon_pos.append([station_core[0] + 0,
    #                   station_core[1] + 0,
    #                   station_core[2] + station_dims[2]])
    #beacon_pos.append([station_core[0] + 0,
    #                   station_core[1] + station_dims[1],
    #                   station_core[2] + station_dims[2]])
    for x_idx in range(3):
        for z_idx in range(2):
            beacon_pos.append([station_core[0] + station_dims[0] * x_idx,
                               station_core[1] + 0,
                               station_core[2] + station_dims[2] * z_idx])
    #beacon_pos.append([station_core[0] + station_dims[0],
    #                   station_core[1] + station_dims[1],
    #                   station_core[2] + station_dims[2]])

    #print("Ground-truth", _x)
    #print("Beacon Locations:" )
    #print(beacon_pos)

    distances = bulk_distance(beacon_pos, _x)
    #print("Distances (SQ)")
    #print(distances)

    start = time.time()
    solution = estimate_nonlin(beacon_pos, distances)
    end = time.time()

    x_predict.append(solution[0])
    y_predict.append(solution[1])
    z_predict.append(solution[2])

    #print("Ground-truth", _x)
    #print("Solution = ", solution)
    #print("Time Elapsed = ", (end - start)*1000, " ms")
    #print("Distance = ", single_point_distance(solution, _x))

    e = single_point_distance(solution, _x)
    error.append(e)
    duration.append(1000 * (end - start))
    #time.sleep(1)

print("Finished Simulation")
#print(error)
#print(xy_loc)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(x_motion, y_motion, z_motion, c='green', marker='^')
ax.scatter(x_predict, y_predict, z_predict, c='red', marker='o')
plt.show()

#fig, actual_plt = plt.subplots()

#color = 'tab:green'
#actual_plt.scatter(x_motion, y_motion, s=duration)

#predict_plt = actual_plt.twinx()
#color = 'tab:red'
#predict_plt.scatter(x_predict, y_predict, z_predict, c='red')
#errplt.set_xlabel('arm length in m')
#errplt.set_ylabel('error (m)', color=color)
#errplt.scatter(xy_loc, error, color=color)
#errplt.tick_params(axis='y', labelcolor=color)

#timeplt = errplt.twinx()
#color = 'tab:blue'
#timeplt.set_ylabel('duration (ms)', color=color)
#timeplt.scatter(xy_loc, duration, color=color)
#timeplt.tick_params(axis='y',labelcolor=color)

#fig.tight_layout()

#plt.show()

#ax.plot3D(x_motion, y_motion, z_motion,'gray')

#plt.show()
