from imports import *

c = constants()

class HRneuronseg:
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

        self.alpha = c.alpha
        self.scale = c.scale
        
        self.xarr = np.zeros(c.iterations)
        self.yarr = np.zeros(c.iterations)
        self.zarr = np.zeros(c.iterations)
        self.parr = np.zeros(c.iterations)

        self.x = -1.6
        self.xR = self.x
        self.y = 4.0
        self.z = 2.75
        self.phi = c.phi
        self.v_syn = c.v_syn
        self.g = c.g

        self.time_vec = np.arange(0, c.ms, c.scale)

        self.connections = []
        self.weights = []
        self.sigmoid = 0.0
        self.sigmoidarr = np.zeros(c.iterations)
        self.k = 10.0
        self.syn = -0.25

        self.garr = np.zeros(c.iterations)
        self.garr += self.g

        self.tarr = np.zeros(c.iterations)
    
    def set_k(self, k):
        self.k = k
    
    def update_tarr(self, time, t):
        self.tarr[time] = t
    
    def update_weights(self, weights):
        self.weights = weights
        self.garr[0] = weights[0]
    
    def get_connections(self):
        return self.connections

    def add_connections(self, neuron):
        if neuron not in self.connections:
            self.connections.append(neuron)
    
    def update_g(self, time, dg):
        self.g = self.g + dg
        self.weights[0] = self.weights[0] + dg
        # print(self.g)
        self.garr[time] = self.g

    def set_current(self, current):
        c.set_current(current)
        self.current = current

    def set_conductance(self, conductance):
        c.set_conductance(conductance)
        self.g = conductance
    
    def set_a(self, a):
        c.set_a(a)
        self.a = a
    
    def set_x(self, x):
        self.x = x
    
    
    def max_sig_func(self, time):
        self.sigmoid = c.clamp(self.x, 0, self.x)
        # print(self.x, self.sigmoid)
        self.sigmoidarr[time] = self.sigmoid

    def sig_func(self, time):
        self.sigmoid = 1 / (1 + np.exp(-self.k * (self.x - self.syn)))
        self.sigmoidarr[time] = self.sigmoid

    def calc_mem(self, phi):
        return (self.alpha + 3 * self.beta * np.abs(phi))
    
    def calculate_init_dx(self):
        return (self.y + (self.b * self.x * self.x) - (self.a * self.x * self.x * self.x) - self.z + self.current)
    
    def calculate_sensory_dx(self, gain, sensory):
        return (self.y + (self.b * self.x * self.x) - (self.a * self.x * self.x * self.x) - self.z + self.current + gain * sensory)

    def calculate_y(self, time):
        dy = self.c - (5 * self.x * self.x) - self.y
        self.y += self.scale * dy
        self.yarr[time] = self.y
    
    def calculate_z(self, time):
        dz = self.r * (self.s * (self.x - self.xR) - self.z)
        self.z += self.scale * dz
        self.zarr[time] = self.z
    
    def update_x(self, time, dx):
        self.x += self.scale * dx
        self.xarr[time] = self.x
    

    
