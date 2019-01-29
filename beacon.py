"""Beacons used to measure distance to a moving object"""
import random
import string
from plotter import Scatters
import numpy as np


class Beacon(object):
    def __init__(self, location, color='black', marker='^', name=None):
        self.location = location
        if name is None:
            self.name = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(6))
        self.color = color
        self.marker = marker

    def get_location(self):
        return self.location[0], self.location[1], self.location[2]

    def draw_beacon(self):
        return Scatters([self.location[0]],
                        [self.location[1]],
                        [self.location[2]],
                        self.color,
                        self.marker)

    def get_distance(self, firefighter):
        """simulate distance reading of a firefighter with noise as function of actual distance"""
        linear_noise = 10
        nonlinear_noise = 0.2
        actual_distance = np.sqrt(np.sum( np.square([self.location[i] - firefighter.location[i] for i in range(3)])))
        return actual_distance * (1 + random.randrange(-1,1) * nonlinear_noise) + random.randrange(-1,1) * linear_noise

