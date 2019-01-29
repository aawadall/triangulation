"""This unit should collect information from beacons, and locates firemen based on information passed"""


class CentralUnit(object):
    """This unit should communicate with all beacons"""

    def __init__(self):
        self.beacons = []  # Beacons registry
        self.firemen = []  # Firemen registry

    def register_fireman(self, fireman):
        self.firemen.append(fireman)

    def register_beacon(self, beacon):
        self.beacons.append(beacon)

    def find_fireman(self, fireman_index):
        #TODO from fireman index, get its location using its beacons
        pass

