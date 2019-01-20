"""An attempt to simulate radio wave propagation in a closed space under abnormal thremal conditions"""
import thread
import time
import numpy as np
import math 

resolution = 0.1  # meters
c = 299792458  # speed of light in m/s
default_frequency = 2.4  # GHz
world_size = [50, 50, 10]  # in meters 

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
        self.velocity = np.zeros(3)  # velocity will be relative to speed of light
        self.frequency = frequency
        self.signal_strength = strength
        self.signal = ''
        
    def emit(self, signal, velocity, signal_strength):
        self.velocity = velocity
        self.signal_strength = signal_strength
        self.signal = signal
        
    
#TODO: create an object: Ether to hold a message at a given frequency for one tick, this object given the frequency can have the message written to it, or read from it. if one tick passes, the message is to be deleted
class Ether(object):
    """array of ether cells"""
    def __init__(self, resolution=resolution, size=world_size):
        self.cells = np.array([[[
            CellSignal() for x in range(world_size[0]*(1/resolution))] 
                         for y in range(world_size[1]*(1/resolution))] 
                         for z in range(world_size[2]*(1/resolution))])
    
    def emit_signal(self, signal, location):
        """create a new signal in point marked in location"""
        index = self.find_location_index(location)
                
    def find_location_index(self, location):
        """a location array could be a vector of real numbers, this function will approximate index""" 
        if 0 <= location[0] <= world_size[0] and \
           0 <= location[1] <= world_size[1] and \
           0 <= location[2] <= world_size[2]:
            return [False,  # Point not outside grid
                    round(location[0] / resolution),  # x index
                    round(location[1] / resolution),  # y index 
                    round(location[2] / resolution)]  # z index 
        else:
            return [True, 0, 0, 0]
        
    def get_propagation_sphere(self, index):
        """from a point in grid, define the sphere of grid cells surrounding that point"""
        radius = resolution
        propagation_sphere = [] 
        for phi in np.arange(0, math.pi *2, resolution):
            for theta in np.arange(0, math.pi * 2, resolution):
                location = [index[0] * resolution + math.cos(phi) * math.sin(theta) * radius,
                            index[1] * resolution + math.sin(phi) * math.sin(theta) * radius,
                            index[2] * resolution + math.cos(theta) * radius]
                index = self.find_location_index(location)
                if not index[0]:
                    propagation_sphere.append(index)
        return list(set(propagation_sphere))
    
def speed_in_medium(medium_index):
    return c / refraction_index[medium_index]

# Refer to https://apps.dtic.mil/dtic/tr/fulltext/u2/a518587.pdf

#TODO: create an object simulator to contain all agents interacting, this object should hold a timer called tick and control objects contained in it

#TODO: create a set of trasmitters, receivers, and transcievers reading and writing Ether