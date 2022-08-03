from imports import *
from HRneuronseg import *

c = constants()

class synapseseg:
    def __init__(self, neurons_list):
        self.neurons = neurons_list
        self.neuron_dict = {}
        self.t1 = 0
        self.t2 = 0

        self.testarr = []
        self.testarr2 = []

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
    
    def update_new_dg2(self, time, const):
        temp1 = []
        temp2 = []
        for i in range(int(len(self.neurons[0].zarr)/10000)):
            temp1.append(self.neurons[0].zarr[10000 * i])

        for i in range(int(len(self.neurons[1].zarr)/10000)):
            temp2.append(self.neurons[1].zarr[10000 * i])
        
        dg = 0
        #temp1[int(time/10000)] - temp1[int(time/10000)-1], temp1[int(time/10000)-1] - temp1[int(time/10000)-2], 
        print(self.testarr)
        print(self.testarr2)
        if (time > 20000):
            # if (temp1[int(time/10000)] - temp1[int(time/10000)-1] < 0):
            #     self.t1 +=10000
            if ((temp1[int(time/10000)] - temp1[int(time/10000)-1] > 0 and temp1[int(time/10000)-1] - temp1[int(time/10000)-2] < 0)
                or (temp1[int(time/10000)] - temp1[int(time/10000)-1] < 0 and temp1[int(time/10000)-1] - temp1[int(time/10000)-2] > 0)):
                if ((self.neurons[0].zarr[time] - self.neurons[0].zarr[time-1] > 0 and self.neurons[0].zarr[time-1] - self.neurons[0].zarr[time-2] < 0)
                    or (self.neurons[0].zarr[time] - self.neurons[0].zarr[time-1] < 0 and self.neurons[0].zarr[time-1] - self.neurons[0].zarr[time-2] > 0)):
                    print("HI")
                    if (len(self.testarr2) > 0 and self.t1 > 10000):
                        dg = -1 * const * ((self.t1*c.scale - self.testarr2[-1]*c.scale) + self.neurons[0].r)
                    if (self.t1 > 10000):
                        self.testarr.append(self.t1)
                    self.t1 = 0
                else:
                    self.t1 += 1
            else:
                self.t1 += 1

            if ((temp2[int(time/10000)] - temp2[int(time/10000)-1] > 0 and temp2[int(time/10000)-1] - temp2[int(time/10000)-2] < 0)
                or (temp2[int(time/10000)] - temp2[int(time/10000)-1] < 0 and temp2[int(time/10000)-1] - temp2[int(time/10000)-2] > 0)):
                if ((self.neurons[1].zarr[time] - self.neurons[1].zarr[time-1] > 0 and self.neurons[1].zarr[time-1] - self.neurons[1].zarr[time-2] < 0)
                    or (self.neurons[1].zarr[time] - self.neurons[1].zarr[time-1] < 0 and self.neurons[1].zarr[time-1] - self.neurons[1].zarr[time-2] > 0)):
                    # print("HI")
                    # if (len(self.testarr) > 0 and self.t1 > 10000):
                    #     dg = const * (np.abs(self.t1*c.scale - self.testarr[-1]*c.scale) + self.neurons[0].r)
                    if (self.t2 > 10000):
                        self.testarr2.append(self.t2)
                    self.t2 = 0
                else:
                    self.t2 += 1
            else:
                self.t2 += 1
            
            # if (temp2[int(time/10000)] - temp2[int(time/10000)-1] < 0):
                # self.t2 +=10000
            # if ((temp2[int(time/10000)] - temp2[int(time/10000)-1] > 0 and temp2[int(time/10000)-1] - temp2[int(time/10000)-2] < 0)
            #     or (temp2[int(time/10000)] - temp2[int(time/10000)-1] < 0 and temp2[int(time/10000)-1] - temp2[int(time/10000)-2] > 0)):
            #     dg = const * (np.abs(self.t1*c.scale - self.*c.scale) + self.neurons[0].r)
            #     self.t2 = 0
            # else:
            #     self.t2 += 10000

        self.neurons[0].update_g(time, dg)
        self.neurons[0].update_tarr(time, self.t1*c.scale)
        self.neurons[1].update_tarr(time, self.t2*c.scale)
        # print (self.neurons[0].weights[0])
        
    
    def update_new_dg(self, time, const):
        dg = 0
        if (self.neurons[0].x < c.inhib):
            self.t1+=1
        elif(self.neurons[0].xarr[time] > c.inhib and self.neurons[0].xarr[time-1] < c.inhib):
            self.t1 = 0
            dg = const * ((self.t1*c.scale - self.t2*c.scale) + self.neurons[0].r)
        
        if (self.neurons[1].x < c.inhib):
            self.t2+=1
        elif(self.neurons[1].xarr[time] > c.inhib and self.neurons[1].xarr[time-1] < c.inhib):
            self.t2 = 0
            dg = const * (np.abs(self.t1*c.scale - self.t2*c.scale) + self.neurons[0].r)
        # for neuron in self.neurons:
        #     neuron.update_g(time, dg)
        self.neurons[0].update_g(time, dg)
        self.neurons[0].update_tarr(time, self.t1*c.scale)
        self.neurons[1].update_tarr(time, self.t2*c.scale)
        print (self.neurons[0].weights[0])

