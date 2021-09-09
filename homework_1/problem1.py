from hopfieldNetwork import *
import numpy as np

patterns = [12, 24, 48, 70, 100, 120]
bits = 120
trials = 10 ** 5
p_errors = []

for p in patterns:
    error = 0
    for i in range(trials):
        network = HopFieldNetwork(p, n_bits=120)
        # set diagonal to 0 depending on which problems homework are we facing
        #np.fill_diagonal(network.w, 0)

        # Choose a random neuron and pattern to feed
        m = np.random.randint(bits)
        p_j = np.random.randint(p)
        input_p = network.patterns[p_j]
        # Feed the network with the pattern and asynchronous rule
        state = network.asynchronousUpdate(input_p, m)
        if (state != input_p[m]):
            error+=1
    p_error = error/trials
    print("P error t=1 %s with %s patterns and %s trials" % (p_error, p, trials))

    p_errors.append(p_error)


