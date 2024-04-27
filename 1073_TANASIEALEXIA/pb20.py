#pb20
import numpy as np
def fitness(x):
    return np.prod(np.abs(x))

def generate_population(n):
    population = np.zeros([n, 7], dtype=int)
    for i in range(n):
        chromosome = np.random.choice([-2, -1, 0, 1, 2, 3, 4], size=6)
        while np.sum(chromosome) >= 10:
            chromosome = np.random.choice([-2, -1, 0, 1, 2, 3, 4], size=6)
        population[i, :6] = chromosome
        population[i, -1] = fitness(chromosome)
    return population

def find_first_lowest_fitness(population):
    min_fitness_index = np.argmin(population[:, -1])
    return population[min_fitness_index, :6]

def find_all_lowest_fitness(population):
    min_fitness = np.min(population[:, -1])
    min_fitness_indices = np.where(population[:, -1] == min_fitness)[0]
    return population[min_fitness_indices, :6]

population = generate_population(8)

print("first individual with lowest fitness")
print(find_first_lowest_fitness(population))

print("all individuals with the lowest fitness")
print(find_all_lowest_fitness(population))
