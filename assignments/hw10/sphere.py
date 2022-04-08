"""
Name: <Olivia Bianco>
<HW10>.py

Problem: <Creating a sphere class.>

Certification of Authenticity:
<I certify that this assignment is entirely my own work.>
"""

import math


class Sphere:

    def __init__(self, radius):
        self.radius = radius
        self.area = 0
        self.sphere_vol = 0

    def get_radius(self):
        return self.radius

    def surface_area(self):  # 4(pi)(r^2)
        self.area = 4 * math.pi * (self.radius ** 2)
        return self.area

    def volume(self):  # 4/3(pi)(r^3)
        self.sphere_vol = (4/3) * math.pi * (self.radius ** 3)
        return self.sphere_vol


