import itertools
import numpy as np
import pyphi
import scipy.stats as stats

def compute_phi(cm, tpm, states, infeasibles):
    j=0
    best_local_phi = 0
    while(j<len(states)):
        try:
            phi = pyphi.compute.phi(pyphi.Subsystem(pyphi.Network(tpm, cm=cm), states[j]))
            if phi > best_local_phi:
                best_local_phi = phi
        except:
            infeasibles = infeasibles + 1
            pass
        j=j+1
    return best_local_phi, infeasibles

if __name__ == '__main__':
    print('Inferring the mean IIT parameter with different number of nodes')
    print('Testing statistical significance of the means. Can it be considered the same?')
    np.random.seed(1)
    nodes_A = 4
    nodes_B = 5
    tpm_dim_A = 2**nodes_A
    tpm_dim_B = 2**nodes_B
    population_size_A = 100
    population_size_B = 100
    infeasibles_A = 0
    infeasibles_B = 0
    print('Population size of number of nodes ' + str(nodes_A) +': ' + str(population_size_A))
    print('Population size of number of nodes ' + str(nodes_B) +': ' + str(population_size_B))
    phis_group_A = np.zeros(population_size_A)
    phis_group_B = np.zeros(population_size_B)
    for i in range(population_size_A):
        tpm_A = np.random.randint(0,2,tpm_dim_A*nodes_A).reshape((tpm_dim_A,nodes_A))
        tpm_B = np.random.randint(0,2,tpm_dim_B*nodes_B).reshape((tpm_dim_B,nodes_B))
        cm_A = np.random.randint(0,2,nodes_A*nodes_A).reshape((nodes_A,nodes_A))
        cm_B = np.random.randint(0,2,nodes_B*nodes_B).reshape((nodes_B,nodes_B))
        states_A = list(itertools.product([0, 1], repeat=nodes_A))
        states_B = list(itertools.product([0, 1], repeat=nodes_B))
        phis_group_A[i], infeasibles_A = compute_phi(cm_A, tpm_A, states_A, infeasibles_A)
        phis_group_B[i], infeasibles_B = compute_phi(cm_B, tpm_B, states_B, infeasibles_B)
        print('Number ' + str(i) + ' of the population computed.')
    print('IIT computation finished')
    print('Results')
    print(phis_group_A)
    print(phis_group_B)

    #Statistics.
    emp_mean_A = np.mean(phis_group_A)
    emp_std_dev_A = np.std(phis_group_A)
    emp_mean_B = np.mean(phis_group_B)
    emp_std_dev_B = np.std(phis_group_B)
   
    ci_width_A = 1.96 * emp_std_dev_A / np.sqrt(population_size_A)
    ci_width_B = 1.96 * emp_std_dev_B / np.sqrt(population_size_B)

    print('Performing two sample t-test. Null hypothesis m1=m2, Alt m1!=m2.')
    print(stats.ttest_ind(a=phis_group_A, b=phis_group_B))

    print('Classic 95% CI for the mean parameter')
    print('Mean for ' + str(nodes_A) + ' nodes: ' + str(emp_mean_A))
    print('95% CI for ' + str(nodes_A) + ' nodes: [' + str(emp_mean_A-ci_width_A) + ',' + str(emp_mean_A+ci_width_A) + '].')
    print('Mean for ' + str(nodes_B) + ' nodes: ' + str(emp_mean_B))
    print('95% CI for ' + str(nodes_B) + ' nodes: [' + str(emp_mean_B-ci_width_B) + ',' + str(emp_mean_B+ci_width_B) + '].')


    print('Infeasible solutions')
    infeasible_A = len(np.where(phis_group_A==0)[0]) + infeasibles_A
    infeasible_B = len(np.where(phis_group_B==0)[0]) + infeasibles_B
    print('Infeasible solutions found for ' + str(nodes_A) + ' nodes: ' + str((infeasibles_A/(population_size_A+infeasibles_A))*100) + '%.')
    print('Infeasible solutions found for ' + str(nodes_B) + ' nodes: ' + str((infeasibles_B/(population_size_B+infeasibles_B))*100) + '%.')
