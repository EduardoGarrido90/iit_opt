import pyphi
import numpy as np
import itertools
import random

def main(D_min, D_max, T, seed, debug=False):
    if debug:
        return None, None, None, None, None, np.random.randint(1, 100, T)
    print('Random search of matrices')
    random.seed(seed)
    best_cm = []
    best_tpm = []
    best_state = []
    best_phi = -1
    individuals = {}
    phis = np.zeros(T)
    i=0
    while(i<T):
        print('Iteration ' + str(i))
        nodes = np.random.randint(D_min, D_max+1)
        states = list(itertools.product([0, 1], repeat=nodes))
        tpm_dim = 2**nodes
        tpm = np.random.randint(0,2,tpm_dim*nodes).reshape((tpm_dim,nodes))
        cm = np.random.randint(0,2,nodes*nodes).reshape((nodes,nodes))
        j=0
        best_local_phi = 0
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
        print(best_phi)
        i=i+1

    print('Random search finished')
    #print('All individuals')
    #print(individuals)
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
