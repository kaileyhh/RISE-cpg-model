from imports import *
from HRneuron import *

c = constants()

class synapse:
    def __init__(self, neurons): # neurons is a list of neurons with this synapse
        self.neurons = neurons
    
    # insert functions here