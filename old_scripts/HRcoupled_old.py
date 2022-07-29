

# import imports
from imports import *

c = constants()

# x(t): membrane potential
# y(t): sodium, potassium transport rate (spiking variable)
# z(t): adaptation current (decreases firing rate after spike)

# I: current, control parameter
# a, b, c, d: modeling of fast ion channels
# r: modeling slow ion channel
# usually s = 4 and xR = -8/5

class HRcoupled:
    def __init__(self, id):
        self.id = id
        self.a = c.a
        self.b = c.b
        self.c = c.c
        self.d = c.c
        self.r = c.r
        self.s = c.s
        self.xR = c.xR
        self.current = c.I
        self.scale = c.scale

        self.rr = c.rr
        self.v = c.v
        self.K = c.K
        self.G = c.G

        self.xarr = np.zeros(c.iterations)
        self.yarr = np.zeros(c.iterations)
        self.zarr = np.zeros(c.iterations)
        self.warr = np.zeros(c.iterations)

        self.x = -1.6
        self.y = 4.0
        self.z = 2.75
        self.w_0 = 1.6
        self.w = self.w_0

    def set_current(self, current):
        c.set_current(current)
        self.current = current
    
    def set_a(self, a):
        c.set_a(a)
        self.a = a
    
    def phi_x(self, x):
        return (-1 * self.a * x**3 + self.b * x**2)
    
    def trident_x(self, x):
        return (self.c - self.d * x**2)

    def calculate_x(self, time):
        dx = self.y + (self.b * self.x * self.x) - (self.a * self.x * self.x * self.x) - self.z + self.current
        self.x += self.scale * dx
        self.xarr[time] = self.x
    
    def calculate_y(self, time):
        dy = self.c - (5 * self.x * self.x) - self.y
        dy = dy - self.G * self.w
        self.y += self.scale * dy
        self.yarr[time] = self.y
    
    def calculate_z(self, time):
        dz = self.r * (self.s * (self.x - self.xR) - self.z)
        self.z += self.scale * dz
        self.zarr[time] = self.z
    
    def calculate_w(self, time):
        dw = self.v * (self.rr * (self.y + self.w_0) - self.K * self.w)
        self.w += self.scale * dw
        self.warr[time] = self.w

    
    # insert formulas and things here
