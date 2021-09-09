import numpy as np
import random
### One-step error probability 2021

# 120 neurons, % de neurones qui ont été changés sur tout les essais

p = [12, 24, 48, 70, 100, 120]
N = 120
trials = 10**5
# our patterns list
patterns = []
one_step_error = []

for number_of_random_pattern in p:
    # each time we generate 12 patterns then 24 then ..

    for i in range (0, trials):
        # initialise state according to the number of neurons
        s_i = np.zeros(N)

        w = np.zeros((N,N)) 
        # loop for each patterns we can do Hebb's rule

        # compute weight for the current number of random patterns
        for i_ in range (0, number_of_random_pattern):
            pattern = np.random.randint(2, size=N)
            pattern = np.where(pattern == 0, -1, 1) # replace the 0 with -1

            # we have to sum and multiple each 
            w = w + np.multiply(pattern, np.transpose(pattern))
        
        # w_j_j = (0,0)
        np.fill_diagonal(w, 0)
        w = w/N

        # update asynchronous randomly choosen single neuron 
        neuron = random.randint(0, number_of_random_pattern)
        activation = w + s_i
        print("Ativation : "+str(activation))
        if (activation == 0):
            activation = 1

        s_i[neuron] = np.sign(activation)

        #print(str(w))
        #print(str(s_i))


    
    # don't forget to empty the patterns list
