from imports import *

c = constants()


class HRcoupled:
    def __init__(self, id):
        self.id = id

        self.a = c.a
        self.b = c.b
        self.c = c.c
        self.d = c.c
        self.r = c.r
        self.s = c.s
        self.current = c.I
        self.scale = c.scale

        self.alpha = 4.0
        self.beta = 5.0
        

        self.xarr = np.zeros(c.iterations)
        self.yarr = np.zeros(c.iterations)
        self.zarr = np.zeros(c.iterations)
        self.parr = np.zeros(c.iterations)

        self.x = -1.6
        self.xR = self.x
        self.y = 4.0
        self.z = 2.75
        self.phi = 0.0
        self.v_syn = -2.0
        self.g = 0.5

        self.time_vec = np.arange(0, c.ms, c.scale)

    def set_current(self, current):
        c.set_current(current)
        self.current = current
    
    def set_a(self, a):
        c.set_a(a)
        self.a = a
    
    def set_x(self, x):
        self.x = x

    def calc_mem(self, phi):
        return (self.alpha + 3 * self.beta * np.abs(phi))
    

    def calculate_x(self, time, s_x):
        # if (self.id < id):
        #     dx = self.y + (self.b * self.x * self.x) - (self.a * self.x * self.x * self.x) - self.z + self.current + weight * self.calc_mem(self.phi) * (self.x - other_x)
        # else:
        #     dx = self.y + (self.b * self.x * self.x) - (self.a * self.x * self.x * self.x) - self.z + self.current + weight * self.calc_mem(self.phi) * (other_x - self.x)
        
        
        dx = self.y + (self.b * self.x * self.x) - (self.a * self.x * self.x * self.x) - self.z + self.current - self.g * (self.x - self.v_syn) * s_x
        self.x += self.scale * dx
        self.xarr[time] = self.x
    
    def calculate_y(self, time):
        dy = self.c - (5 * self.x * self.x) - self.y
        self.y += self.scale * dy
        self.yarr[time] = self.y
    
    def calculate_z(self, time):
        dz = self.r * (self.s * (self.x - self.xR) - self.z)
        self.z += self.scale * dz
        self.zarr[time] = self.z
    
    def calculate_phi(self, time, x, u):
        dphi = (x - u) - self.phi
        self.phi += self.scale * dphi
        self.parr[time] = self.phi




