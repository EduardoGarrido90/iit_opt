#This is going to be the executor of experiments.
import pgrs_algorithm as pgrs
import numpy as np

#Experiment 2:
D_min=3
D_max=5
epsilon=5
p_omega = np.array([0.2,0.3,0.5])
mu=0.2
T=20
pgrs.main(D_min, D_max, epsilon, p_omega, mu, T)
pgrs.test()


