import random
import numpy as np
import scipy.optimize as op

# Initialize Data

x_scale = 100
y_scale = 100
z_scale = 30

scale = [x_scale, y_scale, z_scale]

noise = 0.5

def draw_from_dist(distribution_range):
    return random.randrange(0, #distribution_range * -0.5,
                            distribution_range )

def generate_random_point(_x_scale = x_scale, _y_scale = y_scale, _z_scale = z_scale):
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


# Groundtruth point
_x = generate_random_point()

# beacons
beacon_pos = []

station_dims = [1, 1, 1]

# Station 1
station_core = [-1, -1, 0]
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

# Station 2
station_core = [x_scale / 2, -1, 0]
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

# Station 3
station_core = [x_scale + 1, -1, 0]
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

# Station 4
station_core = [-1, y_scale / 2, 0]
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

# Station 5
station_core = [-1, y_scale + 1, 0]
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

# Station 6
station_core = [-1, -1, z_scale /2]
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

# Station 7
station_core = [-1, -1, z_scale ]
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

print("Ground-truth", _x)
print("Beacon Locations:" )
print(beacon_pos)

distances = bulk_distance(beacon_pos, _x)
print("Distances (SQ)")
print(distances)

def non_lin_cost(x, beacons=beacon_pos, distances=distances):
    #dist_hat = bulk_distance(beacons, x)
    dist_hat = np.sqrt(np.sum(np.square(beacons - x), axis=1))
    return np.sqrt(np.square(distances - dist_hat))

def estimate_nonlin(beacons, distances):
    x_hat = generate_random_point()
    solution = op.least_squares(non_lin_cost, x_hat, verbose=0)
    print("Solution = ",solution.x)


estimate_nonlin(beacon_pos, distances)
print("Ground-truth", _x)
