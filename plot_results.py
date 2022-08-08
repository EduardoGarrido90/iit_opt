#This is going to be the plotting class.
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TKAgg')

def substitute_for_max(results):
    new_results = np.zeros(results.shape[0])
    best = 0
    i=0
    for result in results:
        if result>best:
            best=result
            new_results[i] = result
        else:
            new_results[i] = best
        i=i+1
    return new_results

def plot_simple_experiment(phi_results):
    plt.plot(phi_results)
    plt.xlabel('iterations')
    plt.ylabel('phi')
    plt.title('Best phi over the iterations')
    plt.show()

def plot_mean_and_std_dev(means_1, std_devs_1, means_2, std_devs_2, means_3, std_devs_3):
    iterations = means_1.shape[0]
    x = np.linspace(1, iterations, iterations)
    fig, ax0 = plt.subplots(nrows=1, sharex=True)
    ax0.errorbar(x, means_1, yerr=std_devs_1, fmt='-o', label='PGRS')
    ax0.errorbar(x, means_2, yerr=std_devs_2, fmt='-o', label='RS')
    ax0.errorbar(x, means_3, yerr=std_devs_3, fmt='-o', label='GS')
    ax0.set_title('Best phi over the iterations')
    plt.xlabel('iterations')
    plt.ylabel('phi')
    plt.legend()
    plt.show()

if __name__ == '__main__':
    test_array = np.array([1.2, 2.3, 3.2, 2.3, 3.5, 4.2, 2.1, 2.2, 6.7, 1.1, 9.0, 9.0, 10.0, 11.0, 13.0, 12.0, 1.0])
    #print(substitute_for_max(test_array))
    means = np.array([2.0,3.0,4.0,3.0,2.0,1.0,5.0,2.0])
    std_devs = np.array([0.2, 0.3, 0.4, 0.1, 0.3, 0.4, 0.2, 0.4])
    plot_mean_and_std_dev(means, std_devs, means+1, std_devs-0.1, means-1, std_devs+0.5)
    #plot_simple_experiment(substitute_for_max(test_array))
