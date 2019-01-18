import random
import numpy as np
import scipy.optimize as op

# Initialize Data

x_scale = 500
y_scale = 300
z_scale = 150

scale = [x_scale, y_scale, z_scale]

noise = 5

def simulate_signal(x_fire_figter, x_beacon):
    # Below numbers are subject to modifications, this is initial research
    light_speed = 299792458 # m/s
    reflective_index = [1, # vacum
                        1.000293, #Air
                        1.333, # Water
                        1.52, # Window Glass
                        2.5, #Steel
                        1.458, # Quartz fused
                        2 ] # Concrete

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

station_dims = [1.5, 1.5, 1.5]

# Station 1
station_core = [-50, -50, 0]
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
station_core = [-50, y_scale + 50, 5]
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
