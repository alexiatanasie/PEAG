import numpy as np

def f(x):
    return np.sum(x) % 2 == 0, np.sum(x)

def generate(n):

    individuals_matrix = np.zeros([n, 8], dtype="int")
    i = 0
    while i < n:
        x = np.random.randint(0, 2, 7)
        feasible, val = f(x)
        if feasible:
            individuals_matrix[i, :7] = x
            individuals_matrix[i, -1] = val
            i = i+1
    return individuals_matrix

def pb5():

    n = 19
    individuals = generate(n)
    max_val = np.max(individuals[:, -1])
    max_indices = np.where(individuals[:, -1] == max_val)[0]
    return individuals[max_indices, :7]


print("Chromosomes with the highest fitness:")
print(pb5())
