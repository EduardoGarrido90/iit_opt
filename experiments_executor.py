#This is going to be the executor of experiments.
import pgrs_algorithm as pgrs
import random_search_baseline as rs
import grid_search_baseline as gs
import plot_results as pr
import numpy as np

#Experiment 1:
iterations_experiment = 5
D_min=3
D_max=4
epsilon=5
#p_omega = np.array([0.4,0.3,0.3])
p_omega = np.array([0.4,0.6])
mu=0.1
T=40
#Experiment 2:
#iterations_experiment = 25
#D_min=3
#D_max=5
#epsilon=5
#p_omega = np.array([0.2,0.3,0.5])
#mu=0.2
#T=20
pgrs_results = []
pgrs_best_results = []
rs_results = []
rs_best_results = []
gs_results = []
gs_best_results = []
for iteration in range(iterations_experiment):
    best_phi, best_cm, best_tpm, best_state, individuals, phi_evolution, phis, best_phis = pgrs.main(D_min, D_max, epsilon, p_omega, mu, T, iteration)#, debug=True)
    pgrs_results.append(phis)
    pgrs_best_results.append(best_phis)
    best_phi, best_cm, best_tpm, best_state, individuals, phis, best_phis = rs.main(D_min, D_max, T, iteration)#, debug=True) 
    rs_results.append(phis)
    rs_best_results.append(best_phis)
    best_phi, best_cm, best_tpm, best_state, individuals, phis, best_phis = gs.main(D_min, D_max, T, iteration)#, debug=True)
    gs_results.append(phis)
    gs_best_results.append(best_phis)
mean_pgrs_results = np.mean(pgrs_results, axis=0)
mean_best_pgrs_results = np.mean(pgrs_best_results, axis=0)
mean_rs_results = np.mean(rs_results, axis=0)
mean_best_rs_results = np.mean(rs_best_results, axis=0)
mean_gs_results = np.mean(gs_results, axis=0)
mean_best_gs_results = np.mean(gs_best_results, axis=0)
std_pgrs_results = np.std(pgrs_results, axis=0)
std_best_pgrs_results = np.std(pgrs_best_results, axis=0)
std_rs_results = np.std(rs_results, axis=0)
std_best_rs_results = np.std(rs_best_results, axis=0)
std_gs_results = np.std(gs_results, axis=0)
std_best_gs_results = np.std(gs_best_results, axis=0)
print('PGRS single max across exps.')
print(max([item for sublist in pgrs_results for item in sublist]))
print('RS single max across exps.')
print(max([item for sublist in rs_results for item in sublist]))
print('GS single max across exps.')
print(max([item for sublist in gs_results for item in sublist]))
print('PGRS avg. max.')
print(max(mean_pgrs_results))
print('RS avg. max.')
print(max(mean_rs_results))
print('GS avg. max.')
print(max(mean_gs_results))
import pdb; pdb.set_trace();
pr.plot_simple_experiment(pr.substitute_for_max(mean_pgrs_results))
pr.plot_simple_experiment(pr.substitute_for_max(mean_rs_results))
pr.plot_simple_experiment(pr.substitute_for_max(mean_gs_results))
pr.plot_mean_and_std_dev(mean_pgrs_results, mean_rs_results, mean_gs_results, std_pgrs_results, std_rs_results, std_gs_results)
pr.persist_results('pgrs_2', mean_pgrs_results)
pr.persist_results('rs_2', mean_rs_results)
pr.persist_results('gs_2', mean_gs_results)
