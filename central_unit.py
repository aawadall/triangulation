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

    def find_beacon(self, beaon_index):
        """Given a beacon ID, locate that beacon from known beacons"""
        pass

    def find_fireman(self, fireman_index):
        """Given known beacon locations, find fireman using its distances from identified beacons"""
        observed_distances = []

        # Collect distances vector
        for beacon in self.beacons:
            observed_distances.append(beacon.get_distance(self.firemen[fireman_index]))

        #TODO from fireman index, get its location using its beacons
        pass

