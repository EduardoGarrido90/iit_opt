import pyphi
import numpy as np
import itertools

#transition probability matrix
print('Toy example')
nodes = 3
dimension_size = 2**nodes
tpm = None
found = False
while(not found):
    try:
        tpm = np.random.randint(0,2,dimension_size**2).reshape((dimension_size,dimension_size))
        tpm = tpm/tpm.sum(axis=1,keepdims=1)
        tpm = pyphi.convert.state_by_node2state_by_state(pyphi.convert.state_by_state2state_by_node(np.random.random(dimension_size**2).reshape((dimension_size,dimension_size))))
        found = True
    except:
        pass
print(tpm)
import pdb; pdb.set_trace()
network = pyphi.Network(tpm)

#states
state = (1, 0, 0)

#we need the entire phi of the network.
node_indices = (0,1,2)
subsystem = pyphi.Subsystem(network, state, node_indices)
print(pyphi.compute.phi(subsystem))
