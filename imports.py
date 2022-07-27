import numpy as np
from numpy import random
import matplotlib.pyplot as plt

import scipy
from scipy.io.wavfile import read
from scipy.signal import find_peaks

class constants:
    def __init__(self):
        self.EXAMPLE_CONSTANT = 0
        self.TIME_INCREMENT = 0.0001
        self.OVERALL_TIME = 5

        self.ARR_SIZE = int(self.OVERALL_TIME / self.TIME_INCREMENT)

        # source: https://jamesmccaffrey.wordpress.com/2020/01/27/hindmarsh-rose-model-simulation-using-c-or-python/
        self.a = 1.0
        self.b = 3.0
        self.c = 1.0
        self.d = 5.0
        self.r = 0.006
        self.s = 4.0
        self.xR = -1.6
        self.scale = 0.001
        self.ms = 500
        self.iterations = self.ms * 1000

        self.I = 4.0

        self.rr = 3
        self.v = 0.0009
        self.K = 0.95
        self.G = 0.03

        self.DIP_HEIGHT = -0.1
        self.MIN_HEIGHT = -0.5
        self.MIN_DISTANCE = 5000
        self.ISI_DISTANCE = 100000
        self.MIN_WIDTH = 1

        self.alpha = 4.0
        self.beta = 5.0

        self.phi = 0.0
        self.v_syn = -2.0
        self.g = 10.0

    def set_current(self, current):
        self.I = current
    
    def set_a(self, a):
        self.a = a