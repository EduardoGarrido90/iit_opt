import pyphi
import numpy as np
import itertools

def return_last_batch(phi_evolution, epsilon, i):
    last_batch = []
    init_batch = i - epsilon
    iterations = np.linspace(init_batch, i-1, epsilon)
    for j in range(iterations):
        it = iterations[j]
        last_batch = last_batch.append(phi_evolution[it])
    return last_batch

def update_prior(p_omega, phi_evolution, mu, epsilon, i, D_min):
    phi_results = return_last_batch(phi_evolution, epsilon, i)
    phi_results = sorted(phi_results, reverse=True)
    penalizations = np.linspace(1, -1, len(phi_results)) * mu
    i=0
    for result in phi_results:
        p_omega[result[1]] = p_omega[result[1]] + penalizations[i]
        i=i+1
    #Normalization.
    normalized_p_omega = np.zeros(p_omega.shape[0])
    i=0
    for prior_value in p_omega:
        normalized_p_omega[i] = (prior_value - min(p_omega)) / (max(p_omega) - min(p_omega))
        i=i+1
    return normalized_p_omega

def sample_dimension(D_min, p_omega):
    unif_number = np.random.random()
    acum = 0
    dimension = D_min
    for i in range(len(p_omega)):
        acum = acum + p_omega[i]
        if unif_number < acum:
            dimension = D_min + i
            break
    return dimension

if __name__ == '__main__':
    print('Random search of matrices')
    D_min=3
    D_max=5
    epsilon=5
    p_omega = np.array([0.2,0.3,0.5])
    mu=0.2
    best_cm = []
    best_tpm = []
    best_state = []
    best_phi = -1
    individuals = {}
    phi_evolution = {}
    T = 10
    states = list(itertools.product([0, 1], repeat=nodes))
    while(i<T):
        print('Iteration ' + str(i))
        k=0
        for k in range(0, epsilon):
            nodes = sample_dimension(D_min, p_omega)
            tpm_dim = 2**nodes
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
            phi_evolution[i] = [phi, nodes]
            individuals[i] = [{'phi': best_local_phi}, {'cm' : cm}, {'tpm' : tpm}, {'state': best_local_state}, {'nodes' : nodes}] 
            if best_local_phi > best_phi:
                best_phi = best_local_phi
                best_cm = cm
                best_tpm = tpm
                best_state = best_local_state
            i=i+1
        print('Updating prior distribution')
        p_omega = update_prior(p_omega, phi_evolution, mu, epsilon, i, D_min)

    print('Random search finished')
    print('All individuals')
    print(individuals)
    print('Best result')
    print('phi: ' + str(best_phi))
    print('cm: ' + str(best_cm))
    print('tpm: ' + str(best_tpm))
    print('state: ' + str(best_state))
