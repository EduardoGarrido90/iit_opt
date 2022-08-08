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


if __name__ == '__main__':
    test_array = np.array([1.2, 2.3, 3.2, 2.3, 3.5, 4.2, 2.1, 2.2, 6.7, 1.1, 9.0, 9.0, 10.0, 11.0, 13.0, 12.0, 1.0])
    print(substitute_for_max(test_array))
    plot_simple_experiment(substitute_for_max(test_array))
