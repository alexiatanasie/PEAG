#pb 12

import numpy as np

def calculate_quality(individual):
    return sum(individual[i] for i in range(len(individual)) if i%2 ==0)

def generate_individuals(n):
    individuals = []
    for _ in range(n):
        individual = np.random.randint(0,2,size=8)
        individuals.append(individual)
    return individuals

def calculate_average_quality(individuals):
    total_quality = sum(calculate_quality(individual) for individual in individuals)
    return total_quality / len(individuals)

n =10
individuals = generate_individuals(n)
average_quality = calculate_average_quality(individuals)

print("Matrix:")
for individual in individuals:
    print(individual)

print("Average quality:", average_quality)