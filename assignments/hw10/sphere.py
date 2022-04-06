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

    def get_radius(self):
        return self.radius

    def surface_area(self, radius):  # 4(pi)(r^2)
        return 4 * math.pi * (radius ** 2)

    def volume(self, radius):  # 4/3 * pi * r^3
        return 4/3 * math.pi * (radius ** 3)