"""An attempt to simulate radio wave propagation in a closed space under abnormal thremal conditions"""
import thread
import time
import numpy as np

resolution = 0.1  # meters
c = 299792458  # speed of light in m/s
default_frequency = 2.4  # GHz
world_size = [500, 500, 100]

medium = [
    "vacuum",
    "air",
    "water",
    "glass"
]
refraction_index = [
    1, # vacuum
    1.0003, # air
    1.33, # water
    1.55 # glass
]


class CellSignal(object):
    """Contains information about a signal in an ether cell"""
    def __init__(self, frequency=default_frequency, strength=1):
        self.velocity = np.zeros(3)
        self.frequency = frequency
        self.signal_strength = strength
        
    
#TODO: create an object: Ether to hold a message at a given frequency for one tick, this object given the frequency can have the message written to it, or read from it. if one tick passes, the message is to be deleted
class Ether(object):
    """array of ether cells"""
    def __init__(self, resolution=resolution, size=world_size):
        self.cells = np.array([[[
            CellSignal() for x in range(world_size[0]*(1/resolution))] 
                         for y in range(world_size[1]*(1/resolution))] 
                         for z in range(world_size[2]*(1/resolution))])
        
def speed_in_medium(medium_index):
    return c / refraction_index[medium_index]

# Refer to https://apps.dtic.mil/dtic/tr/fulltext/u2/a518587.pdf

#TODO: create an object simulator to contain all agents interacting, this object should hold a timer called tick and control objects contained in it

#TODO: create a set of trasmitters, receivers, and transcievers reading and writing Ether