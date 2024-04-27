#pb18
import numpy as np

def fitness(x):
    return x[0] + x[1] + x[2] + x[3] - (x[4] + x[5] + x[6] + x[7])

def generate_solutions(n):
    solutions = np.zeros([n, 9], dtype="int")
    for i in range(n):
        valid_solution = False
        while not valid_solution:
            sol = np.random.randint(-1, 2, 8)
            if np.sum(sol[:4]) >= np.sum(sol[4:]):
                valid_solution = True
                solutions[i, :8] = sol
                solutions[i, -1] = fitness(solutions[i, :8])
    return solutions

def max_functie(n):
    solutions = generate_solutions(n)
    max_quality = np.max(solutions[:, -1])
    return max_quality

solutions = generate_solutions(5)
print(solutions)
print(max_functie(5))
