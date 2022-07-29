from imports import *
from HRcoupled import *

c = constants()

class synapse:
    def __init__(self, neurons): # neurons is a list of neurons with this synapse
        self.neurons = neurons
        # self.weights = [[0 for i in len(neurons)] for j in len(neurons)]
        self.neuron1 = self.neurons[0]
        self.neuron2 = self.neurons[1]
        # self.neuron1.set_x(-1)
        self.neuron1.set_current(3.18)

        self.sigmoid1 = 0.0
        self.sigmoid2 = 0.0

        self.sigmoidarr1 = np.zeros(c.iterations)
        self.sigmoidarr2 = np.zeros(c.iterations)

        self.k = 10.0
        self.syn = -0.25

        # self.neuron2.set_x(1.6)
        # self.neuron1.set_current(0)
        # self.neuron2.set_x(1.6)
    
    # def connect_neurons(self, neuron1, neuron2, weight):
    #     if (neuron1.id < neuron2.id):
    #         self.weights[neuron1.id][neuron2.id] = weight
    #     else:
    #         self.weights[neuron2.id][neuron1.id] = weight
    
    def calculate_x(self, time):
        self.neuron1.calculate_x(time, self.sigmoid2)
        self.neuron2.calculate_x(time, self.sigmoid1)
    
    def calculate_y(self, time):
        for neuron in self.neurons:
            neuron.calculate_y(time)
    
    def calculate_z(self, time):
        for neuron in self.neurons:
            neuron.calculate_z(time)

    def calculate_phi(self, time, x, u):
        for neuron in self.neurons:
            neuron.calculate_phi(time, x, u)
    
    def sig_func(self, time):
        self.sigmoid1 = 1 / (1 + np.exp(-self.k * (self.neuron1.x - self.syn)))
        self.sigmoid2 = 1 / (1 + np.exp(-self.k * (self.neuron2.x - self.syn)))
        self.sigmoidarr1[time] = self.sigmoid1
        self.sigmoidarr2[time] = self.sigmoid2

    def calculate_all(self):
        for i in range(c.iterations):
            self.calculate_x(i)
            self.calculate_y(i)
            self.calculate_z(i)
            self.calculate_phi(i, self.neuron1.x, self.neuron2.x)
            self.sig_func(i)

    def graph_all(self):
        fig = plt.figure()
        ax1 = fig.add_subplot(221)
        ax2 = fig.add_subplot(222)
        ax3 = fig.add_subplot(223)
        ax4 = fig.add_subplot(224)

        fig.suptitle("Coupled Inhibitory HR Neurons, Fast Spiking & Bursting")
        
        ax1.plot(self.neuron1.time_vec, self.neuron1.xarr, linewidth=0.5, color="red")
        
        ax2.plot(self.neuron1.time_vec, self.neuron2.xarr, linewidth=0.5, color="green")
        ax3.plot(self.neuron1.time_vec, self.neuron1.xarr, linewidth=0.5, color="red")
        ax3.plot(self.neuron2.time_vec, self.neuron2.xarr, linewidth=0.5, color="green")
        # ax3.plot(self.neuron1.time_vec, self.neuron1.yarr, linewidth=0.5)
        ax4.plot(self.neuron1.time_vec, self.neuron1.sigmoidarr, linewidth=0.5)

        ax1.title.set_text("Neuron 1 (I = " + str(self.neuron1.current) + " ), x0 = " + str(self.neuron1.xR))
        ax1.set_xlabel("time (ms)")
        ax1.set_ylabel("au")
        ax2.title.set_text("Neuron 2 (I = " + str(self.neuron2.current) + " ), x0 = " + str(self.neuron2.xR))
        ax2.set_xlabel("time (ms)")
        ax2.set_ylabel("au")
        ax3.title.set_text("Both")
        ax3.set_xlabel("time (ms)")
        ax3.set_ylabel("au")
        ax4.title.set_text("phi, difference in current")
        ax4.set_xlabel("time (ms)")
        ax4.set_ylabel("au")

        plt.subplots_adjust(left=0.1,
                    bottom=0.1, 
                    right=0.9, 
                    top=0.9, 
                    wspace=0.4, 
                    hspace=0.4)

        # plt.savefig("coupled_neurons_bursting.png", dpi=300)
        plt.savefig("coupled_fast_spiking.png", dpi=300)

        plt.show()
    
    def get_neuron1x(self):
        return self.neuron1.xarr
    
    def get_neuron2x(self):
        return self.neuron2.xarr
    
    def get_neuron1y(self):
        return self.neuron1.yarr
    
    def get_neuron2y(self):
        return self.neuron2.yarr
    
    # insert functions here