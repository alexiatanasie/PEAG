#pb 8
import numpy as np

def generate_population(n, k):
    population = np.zeros((n, k + 1), dtype=int)
    for i in range(n):
        individual = np.random.choice([-4, -3, -2, -1, 1, 2, 3, 4], size=k)  # Generate individual with elements from the given set
        while np.sum(individual) <= 0:  # Ensure the sum of elements is positive
            individual = np.random.choice([-4, -3, -2, -1, 1, 2, 3, 4], size=k)
        quality = np.sum(np.abs(individual))  # Calculate quality as the sum of absolute values of elements
        population[i, :k] = individual
        population[i, -1] = quality
    return population

def min_quality_individuals(population):
    min_quality = np.min(population[:, -1])
    min_quality_individuals = population[population[:, -1] == min_quality]
    return min_quality_individuals

# Example usage
population = generate_population(10, 5)
min_quality_individual = min_quality_individuals(population)
print("Individuals with the lowest quality:")
for individual in min_quality_individual:
    print(individual)
