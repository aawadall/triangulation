import random
import numpy as np
import scipy.optimize as op
import time

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

# beacons
station_dims = [0.9, 0.9, 0.9]

# Station 1
station_core = [-20, -20, 1]
beacon_pos.append([station_core[0] + 0,
                   station_core[1] + 0,
                   station_core[2] + 0])
beacon_pos.append([station_core[0] + station_dims[0],
                   station_core[1] + 0,
                   station_core[2] + 0])
beacon_pos.append([station_core[0] + 0,
                   station_core[1] + station_dims[1],
                   station_core[2] + 0])
beacon_pos.append([station_core[0] + station_dims[0],
                   station_core[1] + station_dims[1],
                   station_core[2] + 0])
beacon_pos.append([station_core[0] + 0,
                   station_core[1] + 0,
                   station_core[2] + station_dims[2]])
beacon_pos.append([station_core[0] + 0,
                   station_core[1] + station_dims[1],
                   station_core[2] + station_dims[2]])
beacon_pos.append([station_core[0] + station_dims[0],
                   station_core[1] + 0,
                   station_core[2] + station_dims[2]])
beacon_pos.append([station_core[0] + station_dims[0],
                   station_core[1] + station_dims[1],
                   station_core[2] + station_dims[2]])

print("Ground-truth", _x)
print("Beacon Locations:" )
print(beacon_pos)

distances = bulk_distance(beacon_pos, _x)
print("Distances (SQ)")
print(distances)

start = time.time()
solution = estimate_nonlin(beacon_pos, distances)
end = time.time()

print("Ground-truth", _x)
print("Solution = ", solution)
print("Time Elapsed = ", (end - start)*1000, " ms")
print("Distance = ", single_point_distance(solution, _x))
