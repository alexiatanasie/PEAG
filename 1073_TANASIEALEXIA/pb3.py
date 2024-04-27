#pb3
import numpy as np
def f(a,x):
    return sum(a[i] * x[i] for i in range(10))

def generare(n,a):
    ind=np.zeros([n, 11], dtype="float")
    for i in range(n):
        x = np.random.uniform(-1, 1, 11)
        if np.sum(x) == 1:
            x = np.random.uniform(-1, 1, 11)
        ind[i, :11] = x
        ind[i, -1] = f(a, x)
    return ind

def max_f(population):
    max_index = np.argmax(population[:, -1])  #
    return population[max_index, :]
def average(population):
    return np.mean(population[:,-1])
def pb3(n, a):
    population = generare(n, a)
    print(population)
    max_individual = max_f(population)
    print("the best ind")
    print(max_individual)
    print("best fitness:", max_individual[-1])
    avg_value = average(population)
    print(avg_value)

a = np.random.uniform(-1, 1, 11)
pb3(10, a)
