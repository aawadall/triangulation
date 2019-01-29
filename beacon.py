"""Beacons used to measure distance to a moving object"""
import random
import string
from plotter import Scatters

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

