"""Beacons used to measure distance to a moving object"""
import random
import string


class Beacon(object):
    def __init__(self, location, color='black', marker='^', name=None):
        self.location = location
        if name is None:
            self.name = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(6))
        self.color = color
        self.marker = marker

    def get_location(self):
        return self.location[0], self.location[1], self.location[2]

    # TODO return scatter object
    # BODY modify all objects to return either a Line or a Scatter object rather than returning locations

