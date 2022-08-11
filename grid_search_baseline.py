import pyphi
import numpy as np
import itertools
import random

def main(D_min, D_max, T, seed, debug=True):
    if debug:
        return None, None, None, None, None, np.random.randint(1, 100, T)
    print('Grid search of matrices')
    random.seed(seed)
    best_cm = []
    best_tpm = []
    best_state = []
    best_phi = -1
    individuals = {}
    phis = np.zeros(T)
    space_range = D_max - D_min + 1
    iterations_for_dimension = T/float(space_range)
    nodes_array = np.repeat(np.linspace(D_min, D_max, space_range), iterations_for_dimension)
    tpms = {}
    for sp in range(space_range):
        current_dimension = sp + D_min
        tpm_x = 2**current_dimension
        tpm_y = current_dimension
        columns = np.array([np.binary_repr(i, width=2**tpm_x) for i in np.linspace(0, 2**tpm_x, tpm_y*iterations_for_dimension).astype(int)])
        tpms[current_dimension] = np.array([np.fromstring(" ".join(i), sep=" ") for i in columns]).T
    dimension_index_tpm = 0
    previous_node=0
    i=0
    while(i<T):
        print('Iteration ' + str(i))
        nodes = nodes_array[i]
        states = list(itertools.product([0, 1], repeat=nodes))
        tpm_dim = 2**nodes
        if previous_node != 0 and previous_node != nodes:
            dimension_index_tpm=0
        previous_node = nodes
        tpm = tpms[nodes][:,dimension_index_tpm:dimension_index_tpm+tpm_y]
        dimension_index_tpm = dimension_index_tpm + tpm_y
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
        individuals[i] = [{'phi': best_local_phi}, {'cm' : cm}, {'tpm' : tpm}, {'state': best_local_state}, {'nodes' : nodes}] 
        phis[i] = best_local_phi
        if best_local_phi > best_phi:
            best_phi = best_local_phi
            best_cm = cm
            best_tpm = tpm
            best_state = best_local_state
        i=i+1

    print('Grid search finished')
    print('All individuals')
    print(individuals)
    print('Best result')
    print('phi: ' + str(best_phi))
    print('cm: ' + str(best_cm))
    print('tpm: ' + str(best_tpm))
    print('state: ' + str(best_state))
    return best_phi, best_cm, best_tpm, best_state, individuals, phis

def test():
    print('It works')

if __name__ == '__main__':
    D_min=3
    D_max=5
    T=20
    seed=1
    main(D_min, D_max, T, seed)
