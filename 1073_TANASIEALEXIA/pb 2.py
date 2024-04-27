#pb 2
import numpy as np

def fitness(individual):
    quality = 0
    for i in range(len(individual) - 1):
        if individual[i] != individual[i+1]:
            quality += 1
    return quality

def generate_pop(n):
    population = np.zeros((n, 6), dtype=int)
    for i in range(n):
        individual = np.random.randint(0, 2, 5)
        quality = fitness(individual)
        population[i, :5] = individual
        population[i, -1] = quality
    return population

def max_quality_fitness(population):
    max_quality = np.max(population[:, -1])
    max_quality_individuals = population[population[:, -1] == max_quality]
    return max_quality_individuals

# Example usage
population = generate_pop(18)
max_quality_individuals = max_quality_fitness(population)
print("Individuals with the highest quality:")
for individual in max_quality_individuals:
    print(individual)


