#pb9
import random

def generate_individual(k):
    individual = [random.randint(0, 1) for _ in range(k)]
    quality = sum(1 for i in range(k-1) if individual[i] == individual[i+1])
    return individual + [quality]

def generate_population(k, num_individuals=10):
    return [generate_individual(k) for _ in range(num_individuals)]

def evaluate_population(population):
    population.sort(key=lambda individual: individual[-1])
    for individual in population:
        print(individual)

k = 5
population = generate_population(k)
evaluate_population(population)