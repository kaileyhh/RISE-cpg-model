from imports import *
from HRneuronseg import *

c = constants()

class synapseseg:
    def __init__(self, neurons_list):
        self.neurons = neurons_list
        self.neuron_dict = {}
        self.t1 = 0
        self.t2 = 0

        for neuron in self.neurons:
            self.neuron_dict.update({str(neuron.id): neuron})
    
    def add_neuron(self, neuron):
        if neuron not in self.neurons:
            self.neurons.append(neuron)
            self.neuron_dict.update({str(neuron.id): neuron})
    
    def attach_neurons(self, neuron, neuron_att):
        neuron.add_connections(neuron_att.id)
    
    def get_neuron(self, id):
        return (self.neuron_dict.get(str(id)))
    
    def calculate_x(self, neuron, time):
        connections = neuron.get_connections()
        dx = neuron.calculate_init_dx()
        if (len(connections) > 0):
            for i in connections:
                dx -= neuron.g * (neuron.x - neuron.v_syn) * self.get_neuron(i).sigmoid
        neuron.update_x(time, dx)
    
    def calculate_max_x(self, neuron, time):
        connections = neuron.get_connections()
        dx = neuron.calculate_init_dx()
        if (len(connections) > 0):
            for i in connections:
                dx -= neuron.g * (neuron.x - neuron.v_syn) * self.get_neuron(i).sigmoid
        neuron.update_x(time, dx)
    
    def calculate_sensory_x(self, neuron, time, gain, sensory, weight):
        # - weight = excitatory, +weight = inhibitory
        connections = neuron.get_connections()
        dx = neuron.calculate_sensory_dx(gain, sensory)
        if (len(connections) > 0):
            for i in connections:
                dx -= weight * (neuron.x - neuron.v_syn) * self.get_neuron(i).sigmoid
        neuron.update_x(time, dx)

    def calculate_weight_x(self, neuron, time):
        connections = neuron.get_connections()
        dx = neuron.calculate_init_dx()
        if (len(connections) > 0):
            for i in range(len(connections)):
                dx -= neuron.weights[i] * (neuron.x - neuron.v_syn) * self.get_neuron(connections[i]).sigmoid
        neuron.update_x(time, dx)

    
    def calculate_all(self, time):
        for neuron in self.neurons:
            self.calculate_x(neuron, time)
            neuron.calculate_y(time)
            neuron.calculate_z(time)
            neuron.sig_func(time)
    
    def calculate_max_all(self, time):
        for neuron in self.neurons:
            self.calculate_x(neuron, time)
            neuron.calculate_y(time)
            neuron.calculate_z(time)
            neuron.max_sig_func(time)
    
    def calculate_sensory_all(self, time, gain, sensory, id):
        for neuron in self.neurons:
            if (neuron.id == id):
                self.calculate_sensory_x(neuron, time, gain, sensory, 1.0)
            else:
                self.calculate_x(neuron, time)
            neuron.calculate_y(time)
            neuron.calculate_z(time)
            neuron.sig_func(time)
    
    def create_weight_mat(self, neuron, weight_list):
        neuron.update_weights(weight_list)

    def calculate_weight_all(self, time):
        for neuron in self.neurons:
            self.calculate_weight_x(neuron, time)
            neuron.calculate_y(time)
            neuron.calculate_z(time)
            neuron.sig_func(time)
    
    def update_dg(self, time, const):
        dg = const * np.abs(self.neurons[0].current - self.neurons[1].current)
        for neuron in self.neurons:
            neuron.update_g(time, dg)
    
    def update_new_dg(self, time, const):
        if (self.neurons[0].x < -1.0):
            self.t1+=1
        else:
            self.t1 = 0
        if (self.neurons[1].x < -1.0):
            self.t2+=1
        else:
            self.t2 = 0
        dg = const * (np.abs(self.t1*c.scale - self.t2*c.scale) + self.neurons[0].r)
        for neuron in self.neurons:
            neuron.update_g(time, dg)
        print (self.neurons[0].g)

