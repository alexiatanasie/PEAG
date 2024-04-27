#pb7
import numpy as np
def fitness(x):
    return np.sum(x)

def generate_individual():

    individual = np.random.randint(0, 2, 6)
    return individual

def generate_population(n):

    population = np.zeros((n, 7), dtype=int)
    for i in range(n):
        individual = generate_individual()
        fitness_val = fitness(individual)
        population[i, :6] = individual
        population[i, -1] = fitness_val
    return population

def find_individual_with_lowest_fitness(population):

    min_fitness_index = np.argmin(population[:, -1])
    return population[min_fitness_index, :6]

def find_individuals_with_lowest_fitness(population):

    min_fitness = np.min(population[:, -1])
    min_fitness_indices = np.where(population[:, -1] == min_fitness)[0]
    return population[min_fitness_indices, :6]

n = 8
population = generate_population(n)

print("the first ind with the lowest fitness:")
print(find_individual_with_lowest_fitness(population))

print("all ind with the lowest fitness")
print(find_individuals_with_lowest_fitness(population))
