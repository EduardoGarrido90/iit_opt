import pyphi
import numpy as np
import itertools

#transition probability matrix
print('Toy example')
tpm = np.array([[0, 0, 0], [0, 0, 1], [1, 0, 1], [1, 0, 0], [1, 1, 0], [1, 1, 1], [1, 1, 1], [1, 1, 0]])
print(tpm.shape)

#connectivity matrix
cm = np.array([[0,0,1],[1,0,1],[1,1,0]])
labels = ('A', 'B', 'C')
print(cm.shape)

#network
network = pyphi.Network(tpm, cm=cm, node_labels=labels)

#states
state = (1, 0, 0)

#we need the entire phi of the network.
node_indices = (0,1,2)
subsystem = pyphi.Subsystem(network, state, node_indices)
print(pyphi.compute.phi(subsystem))


print('Random search of matrices')
nodes=5
best_cm = []
best_tpm = []
best_state = []
best_phi = -1
individuals = {}
iterations_search = 10
states = list(itertools.product([0, 1], repeat=nodes))
tpm_dim = 2**nodes
for i in range(0, iterations_search):
   print('Iteration ' + str(i))
   tpm = np.random.randint(0,2,tpm_dim*nodes).reshape((tpm_dim,nodes))
   cm = np.random.randint(0,2,nodes*nodes).reshape((nodes,nodes))
   j=0
   best_local_phi = -1
   best_local_state = states[0]
   while(j<len(states)):
       try:
           phi = pyphi.compute.phi(pyphi.Subsystem(pyphi.Network(tpm, cm=cm), states[j]))
           if phi > best_local_phi:
               best_local_phi = phi
               best_local_state = states[j]
       except:
           pass
       j=j+1
   if best_local_phi > best_phi:
       best_phi = best_local_phi
       best_cm = cm
       best_tpm = tpm
       best_state = best_local_state

   individuals[i] = [{'phi': best_local_phi}, {'cm' : cm}, {'tpm' : tpm}, {'state': best_local_state}] 

print('Random search finished')
print('All individuals')
print(individuals)
print('Best result')
print('phi: ' + str(best_phi))
print('cm: ' + str(best_cm))
print('tpm: ' + str(best_tpm))
print('state: ' + str(best_state))
