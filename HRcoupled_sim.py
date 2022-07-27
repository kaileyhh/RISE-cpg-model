from imports import *
from HRcoupled import *
from HRneuron import *
from synapse import *

c = constants()

neuron1 = HRcoupled(1) 
neuron2 = HRcoupled(2)

time_vec = np.arange(0, c.ms, c.scale)
current_vec = np.zeros(c.iterations) + c.I

synapse1 = synapse([neuron1, neuron2])

synapse1.calculate_all()

# print(synapse1.sigmoid1)
synapse1.graph_all()