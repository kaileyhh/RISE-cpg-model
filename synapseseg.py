from imports import *
from HRneuronseg import *

c = constants()

class synapseseg:
    def __init__(self, neurons_list):
        self.neurons = neurons_list
        self.neuron_dict = {}

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
            
    
    def calculate_all(self, time):
        for neuron in self.neurons:
            self.calculate_x(neuron, time)
            neuron.calculate_y(time)
            neuron.calculate_z(time)
            neuron.sig_func(time)