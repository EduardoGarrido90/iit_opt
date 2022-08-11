#This is going to be the executor of experiments.
import pgrs_algorithm as pgrs
import random_search_baseline as rs
import grid_search_baseline as gs
import plot_results as pr
import numpy as np

#Experiment 1:
iterations_experiment = 25
D_min=3
D_max=4
epsilon=5
p_omega = np.array([0.2,0.8])
mu=0.5
T=10
#Experiment 2:
#iterations_experiment = 25
#D_min=3
#D_max=5
#epsilon=5
#p_omega = np.array([0.2,0.3,0.5])
#mu=0.2
#T=20
pgrs_results = []
rs_results = []
gs_results = []
for iteration in range(iterations_experiment):
    import pdb; pdb.set_trace();
    best_phi, best_cm, best_tpm, best_state, individuals, phi_evolution, phis = pgrs.main(D_min, D_max, epsilon, p_omega, mu, T, iteration)#, debug=True)
    pgrs_results.append(phis)
    best_phi, best_cm, best_tpm, best_state, individuals, phis = rs.main(D_min, D_max, T, iteration, debug=True) 
    rs_results.append(phis)
    best_phi, best_cm, best_tpm, best_state, individuals, phis = gs.main(D_min, D_max, T, iteration, debug=True)
    gs_results.append(phis)
mean_pgrs_results = np.mean(pgrs_results, axis=0)
mean_rs_results = np.mean(rs_results, axis=0)
mean_gs_results = np.mean(gs_results, axis=0)
std_pgrs_results = np.std(pgrs_results, axis=0)
std_rs_results = np.std(rs_results, axis=0)
std_gs_results = np.std(gs_results, axis=0)
pr.plot_mean_and_std_dev(mean_pgrs_results, mean_rs_results, mean_gs_results, std_pgrs_results, std_rs_results, std_gs_results)
pr.persist_results('pgrs_2', mean_pgrs_results)
pr.persist_results('rs_2', mean_rs_results)
pr.persist_results('gs_2', mean_gs_results)
