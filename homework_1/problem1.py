from hopfieldNetwork import *
import numpy as np

patterns = [12, 24, 48, 70, 100, 120]
bits = 120
trials = 10 ** 5
p_error = []


for p in patterns:
    error = 0
    for i in range(trials):
        network = HopFieldNetwork(p, n_bits=120)
        # set diagonal to 0
        np.fill_diagonal(network.w, 0)

        # Choose a random neuron



