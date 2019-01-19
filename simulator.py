"""An attempt to simulate radio wave propagation in a closed space under abnormal thremal conditions"""
import thread
import time

c = 299792458 # speed of light in m/s

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

def speed_in_medium(medium_index):
    return c / refraction_index[medium_index]

# Refer to https://apps.dtic.mil/dtic/tr/fulltext/u2/a518587.pdf

#TODO: create an object simulator to contain all agents interacting, this object should hold a timer called tick and control objects contained in it
#TODO: create an object: Ether to hold a message at a given frequency for one tick, this object given the frequency can have the message written to it, or read from it. if one tick passes, the message is to be deleted
#TODO: create a set of trasmitters, receivers, and transcievers reading and writing Ether