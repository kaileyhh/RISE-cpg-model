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

        self.warr = []
        self.warr2 = []

        self.peaks_arr = []
        self.time_arr = []

        self.time_arr1 = []
        self.time_arr2 = []

        self.everything1 = []
        self.everything2 = []
        
        self.swaps = []

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

    def calculate_if_peak(self, neuron, time):
        if (time < 2):
            return False
        neg_deriv = neuron.xarr[time] - neuron.xarr[time-1] < 0
        pos_deriv = neuron.xarr[time-1] - neuron.xarr[time-2] > 0
        if (neg_deriv and pos_deriv and neuron.xarr[time] > 1):
            return True
        return False
    
    def calculate_if_anti_peak(self, neuron, time):
        if (time < 2):
            return False
        neg_deriv = neuron.xarr[time] - neuron.xarr[time-1] < 0
        pos_deriv = neuron.xarr[time-1] - neuron.xarr[time-2] > 0
        if (neg_deriv and pos_deriv and neuron.xarr[time] < 0):
            return True
        return False
    
    def update_dg_peaks(self, time, const):
        dg = 0
        # print(len(self.peaks_arr), len(self.time_arr))
        print(self.everything1)
        print(self.everything2)
        

        peak = self.calculate_if_peak(self.neurons[0], time)
        anti_peak = self.calculate_if_anti_peak(self.neurons[0], time)
        if (peak and time > 20000):
            
            # if (len(self.time_arr2) > 0):
            #     self.time_arr.append(time - self.time_arr2[-1])
            # else:
            #     self.time_arr.append(time)
            
            self.time_arr.append(time)
            self.time_arr1.append(time)

            if (len(self.peaks_arr) > 0):
                if (self.peaks_arr[-1] == -1):
                    self.swaps.append(time)
                    # self.everything1.append(self.time_arr1[-1] - self.time_arr2[-1])
                    if (len(self.swaps) >= 3):
                        self.everything1.append(self.swaps[-1] - self.swaps[-2])
                        self.everything2.append(self.swaps[-2] - self.swaps[-3])
                        dg = -1 * const * (((self.everything1[-1] - self.everything2[-1])*c.scale) + c.kappa)
            
            self.peaks_arr.append(1)

        if (anti_peak and time > 20000):
            self.time_arr.append(time)
            self.time_arr2.append(time)
        
            if (len(self.peaks_arr) > 0):
                if (self.peaks_arr[-1] == 1):
                    self.swaps.append(time)
                    # if (len(self.swaps) >= 2):
                    #     self.everything2.append(self.swaps[-1] - self.swaps[-2])
                    
            self.peaks_arr.append(-1)

            # if (len(self.time_arr1) > 0):
            #     self.time_arr.append(time - self.time_arr1[-1])
            # else:
            #     self.time_arr.append(time)
            
        self.neurons[0].update_g(time, dg)

    def update_new_dg2(self, time, const):
        temp1 = []
        temp2 = []
        for i in range(int(len(self.neurons[0].zarr)/10000)):
            temp1.append(self.neurons[0].zarr[10000 * i])

        for i in range(int(len(self.neurons[1].zarr)/10000)):
            temp2.append(self.neurons[1].zarr[10000 * i])
        
        dg = 0
        #temp1[int(time/10000)] - temp1[int(time/10000)-1], temp1[int(time/10000)-1] - temp1[int(time/10000)-2], 
        print(self.testarr, self.warr)
        print(self.testarr2, self.warr2)
        if (True):
            # if (temp1[int(time/10000)] - temp1[int(time/10000)-1] < 0):
            #     self.t1 +=10000
            if ((temp1[int(time/10000)] - temp1[int(time/10000)-1] > 0 and temp1[int(time/10000)-1] - temp1[int(time/10000)-2] < 0)):
                if ((self.neurons[0].zarr[time] - self.neurons[0].zarr[time-1] > 0 and self.neurons[0].zarr[time-1] - self.neurons[0].zarr[time-2] < 0)):
                    # print("HI")
                    if (self.t1 > 10000 and len(self.warr) > 0):
                        # dg = -1 * const * ((self.t1*c.scale - self.testarr2[-1]*c.scale) + c.kappa)
                        dg = -1 * const * ((self.t1*c.scale - (time - self.warr[-1]/c.scale - self.t1)*c.scale) + c.kappa)
                        self.testarr2.append(time - self.warr[-1]/c.scale - self.t1)
                    if (self.t1 > 10000):
                        self.testarr.append(self.t1)

                        self.warr.append(int(time*c.scale))
                        self.t1 = 0
                elif (self.neurons[0].zarr[(time)] - self.neurons[0].zarr[(time)-1] < 0):
                    self.t1 += 1
                # else:
                #     self.t1 = 0
            elif (self.neurons[0].zarr[(time)] - self.neurons[0].zarr[(time)-1] < 0):
                self.t1 += 1
            
            # if ((temp2[int(time/10000)] - temp2[int(time/10000)-1] > 0 and temp2[int(time/10000)-1] - temp2[int(time/10000)-2] < 0)):
            #     if ((self.neurons[1].zarr[time] - self.neurons[1].zarr[time-1] > 0 and self.neurons[1].zarr[time-1] - self.neurons[1].zarr[time-2] < 0)):
            #         # print("HI")
            #         # if (len(self.te) > 0 and self.t1 > 10000):
            #         #     dg = -1 * const * ((self.t1*c.scale - self.testarr2[-1]*c.scale) + c.kappa)
            #         if (self.t2 > 3000):
            #             self.testarr2.append(self.t2)
            #             self.warr2.append(int(time*c.scale))
            #             self.t2 = 0
            #     elif (self.neurons[1].zarr[(time)] - self.neurons[1].zarr[(time)-1] < 0):
            #         self.t2 += 1
            #     # else:
            #     #     self.t1 = 0
            # elif (self.neurons[1].zarr[(time)] - self.neurons[1].zarr[(time)-1] < 0):
            #     self.t2 += 1
            
            # if ((temp1[int(time/10000)] - temp1[int(time/10000)-1] < 0 and temp1[int(time/10000)-1] - temp1[int(time/10000)-2] > 0)):
            #     if ((self.neurons[0].zarr[time] - self.neurons[0].zarr[time-1] < 0 and self.neurons[0].zarr[time-1] - self.neurons[0].zarr[time-2] > 0)):
            #         print("HI")
            #         # if (len(self.testarr2) > 0 and self.t2 > 10000):
            #         #     dg = -1 * const * ((self.t1*c.scale - self.testarr2[-1]*c.scale) + c.kappa)
            #         self.testarr2.append(self.t2)
            #         self.warr2.append(int(time*c.scale))
            #         self.t2 = 0
            #     else:
            #         self.t2 += 1
            # elif (self.neurons[0].zarr[(time)] - self.neurons[0].zarr[(time)-1] > 0):
            #     self.t2 += 1
                # else:
                #     self.t1 = 0
            
            # elif (self.neurons[0].zarr[(time)] - self.neurons[0].zarr[(time)-1] > 0):
            #     self.t2 += 1


            # if ((temp2[int(time/10000)] - temp2[int(time/10000)-1] > 0 and temp2[int(time/10000)-1] - temp2[int(time/10000)-2] < 0)):
            #     if ((self.neurons[1].zarr[time] - self.neurons[1].zarr[time-1] > 0 and self.neurons[1].zarr[time-1] - self.neurons[1].zarr[time-2] < 0)):
            #         # print("HI")
            #         # if (len(self.testarr) > 0 and self.t1 > 10000):
            #         #     dg = const * (np.abs(self.t1*c.scale - self.testarr[-1]*c.scale) + self.neurons[0].r)
            #         if (self.t2 > 10000):
            #             self.testarr2.append(self.t2)
            #             self.warr2.append(int(time*c.scale))
            #         self.t2 = 0
            #     elif (self.neurons[1].zarr[(time)] - self.neurons[1].zarr[(time)-1] < 0):
            #         self.t2 += 1
            #     # else:
            #     #     self.t2 = 0
            # elif (self.neurons[1].zarr[(time)] - self.neurons[1].zarr[(time)-1] < 0):
            #     self.t2 += 1
            
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

