#pb13
import numpy as np

def f(a, x):
    return sum(a[i] * x[i] for i in range(7))

def gen(n, a):
    ind = np.zeros([n, 8], dtype="float")  #8th element-fitness
    for i in range(n):
        x = np.random.uniform(-10, 10, 7)
        while np.sum(x) <= 10:
            x = np.random.uniform(-10, 10, 7)
        ind[i, :7] = x
        ind[i, -1] = f(a, x)
    return ind

def max_f(population):
    max_index = np.argmax(population[:, -1])
    return population[max_index, :]

def pb(n, a):
    population = gen(n, a)
    print("generate population:")
    print(population)
    max_individual = max_f(population)
    print("the max ind")
    print(max_individual)
    print("max quality:", max_individual[-1])

a = np.random.uniform(-10, 10, 7)
pb(10, a)
