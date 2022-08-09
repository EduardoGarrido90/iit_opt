#This is going to be the executor of experiments.
import pgrs_algorithm as pgrs
import random_search_baseline as rs
import grid_search_baseline as gs
import numpy as np

#Experiment 2:
iterations_experiment = 25
D_min=3
D_max=5
epsilon=5
p_omega = np.array([0.2,0.3,0.5])
mu=0.2
T=20
pgrs_results = []
rs_results = []
gs_results = []
for iteration in range(iterations_experiment):
    best_phi, best_cm, best_tpm, best_state, individuals, phi_evolution, phis = pgrs.main(D_min, D_max, epsilon, p_omega, mu, T, iteration, debug=True)
    pgrs_results.append(phis)
    best_phi, best_cm, best_tpm, best_state, individuals, phis = rs.main(D_min, D_max, T, iteration, debug=True) 
    rs_results.append(phis)
    best_phi, best_cm, best_tpm, best_state, individuals, phis = gs.main(D_min, D_max, T, iteration, debug=True)
    gs_results.append(phis)
import pdb; pdb.set_trace();
