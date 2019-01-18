"""An attempt to simulate radio wave propagation in a closed space under abnormal thremal conditions"""
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