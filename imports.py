import numpy as np
from numpy import random
import matplotlib.pyplot as plt

class constants:
    def __init__(self):
        self.EXAMPLE_CONSTANT = 0
        self.TIME_INCREMENT = 0.0001
        self.OVERALL_TIME = 5

        self.ARR_SIZE = int(self.OVERALL_TIME / self.TIME_INCREMENT)

        # HR NEURON, from wikipedia :>

        # self.FIXED_S = 4.0
        # self.FIXED_XR = -8/5
        # self.FIXED_A = 1.0
        # self.FIXED_B = 3.0
        # self.FIXED_C = 1.0
        # self.FIXED_D = 5.0
        # self.FIXED_R = 10e-3

        
        # source: https://jamesmccaffrey.wordpress.com/2020/01/27/hindmarsh-rose-model-simulation-using-c-or-python/
        self.a = 1.0
        self.b = 3.0
        self.c = 1.0
        self.d = 5.0
        self.r = 0.005
        self.s = 4.0
        self.xR = -1.6
        self.scale = 0.001
        self.ms = 200
        self.iterations = self.ms * 1000
        self.I = 5
