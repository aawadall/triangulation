"""Beacons used to measure distance to a moving object"""
import random
import string


class Beacon(object):
    def __init__(self, location, name=None, color='black', marker='^'):
        self.location = location
        if name is None:
            self.name = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(6))
        self.color = color
        self.marker = '^'
