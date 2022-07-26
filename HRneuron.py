

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

class HRneuron:
    def __init__(self, id):
        self.id = id
        # self.s = c.FIXED_S
        # self.xR = c.FIXED_XR
        # self.dt = c.TIME_INCREMENT

        # self.a = c.FIXED_A
        # self.b = c.FIXED_B
        # self.c = c.FIXED_C
        # self.d = c.FIXED_D
        # self.r = c.FIXED_R

        self.a = c.a
        self.b = c.b
        self.c = c.c
        self.d = c.c
        self.r = c.r
        self.s = c.s
        self.xR = c.xR
        self.current = c.I
        self.scale = c.scale

        # self.I = current
        # self.x = np.zeros(c.ARR_SIZE)
        # self.x[0] = -1.6
        # self.y = np.zeros(c.ARR_SIZE)
        # self.y[0] = 4.0
        # self.z = np.zeros(c.ARR_SIZE)
        # self.z[0] = 2.75

        self.xarr = np.zeros(c.iterations)
        self.yarr = np.zeros(c.iterations)
        self.zarr = np.zeros(c.iterations)

        self.x = -1.6
        self.y = 4.0
        self.z = 2.75

    def set_current(self, current):
        c.set_current(current)
        self.current = current
    
    def phi_x(self, x):
        return (-1 * self.a * x**3 + self.b * x**2)
    
    def trident_x(self, x):
        return (self.c - self.d * x**2)

    def calculate_x(self, time):
        dx = self.y + (self.b * self.x * self.x) - (self.a * self.x * self.x * self.x) - self.z + self.current
        self.x += self.scale * dx
        self.xarr[time] = self.x
        # self.x[time] = self.x[time-1] + (self.y[time-1] + self.phi_x(self.x[time-1]) - self.z[time-1] + self.I[time]) * self.dt 
    
    def calculate_y(self, time):
        dy = self.c - (5 * self.x * self.x) - self.y
        self.y += self.scale * dy
        self.yarr[time] = self.y
        # self.y[time] = self.y[time-1] + (self.trident_x(self.x[time-1]) - self.y[time-1]) * self.dt
    
    def calculate_z(self, time):
        dz = self.r * (self.s * (self.x - self.xR) - self.z)
        self.z += self.scale * dz
        self.zarr[time] = self.z
        # self.z[time] = self.z[time-1] + (self.r * (self.s * (self.x[time-1] - self.xR) - self.z[time-1])) * self.dt

    
    # insert formulas and things here
