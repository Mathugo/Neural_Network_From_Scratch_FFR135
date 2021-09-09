# hugo math
# hopfieldNetwork.py

import numpy as np
import random

def genPatterns(patterns, n_bits):
    # generate random vector with -1 or 1 int value
    return np.random.randint(2, size=(patterns, n_bits)) *2 -1

class HopFieldNetwork:
    def __init__(self, patterns=1, n_bits=120):
        # generate patterns
        self.n_bits = n_bits
        self.w = np.zeros((n_bits,n_bits))
        self.patterns = genPatterns(patterns, n_bits)
        self.calcWeights()
    
    def calcWeights(self):
        # calcul the wheight for each patterns
        for p in self.patterns:
            one_array_p = p.reshape(self.n_bits,1)
            # shape (n_bits, 1) vector    
            self.w = self.w + one_array_p @ np.transpose(one_array_p)      
            # W_i_j = Sum(x.xT) : Matrix multiplication
        self.w = 1/self.n_bits * self.w
    
    def asynchronousUpdate(self, input, neuron_index_m):
        neuron_w = self.w[neuron_index_m, :]
        activation = neuron_w @ input
        s_i = np.sign(activation) 
        if s_i == 0:
            s_i = 1
        return s_i
        