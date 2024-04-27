#pb11
import numpy as np

def calculate_quality(x, y, z):
    t = x + y - z
    return t * x**2 - 2 * y * z

def generate_population(n):
    population = []
    for _ in range(n):
        x = np.random.uniform(-2,2)
        y = np.random.uniform(-2,2)
        z = np.random.uniform(-2,2)
        while x + y - z != 0:
            x = np.random.uniform(-2, 2)
            y = np.random.uniform(-2, 2)
            z = np.random.uniform(-2, 2)
        population.append((x,y,z))
    return population

def evaluate_population(population):
    qualities = []
    for individual in population:
        x,y,z = individual
        quality = calculate_quality(x,y,z)
        qualities.append(quality)
    return qualities

def display_pop_and_max_quality(qualities):
    print("Population:")
    for i, individual in enumerate(population):
        print(i + 1, ":", individual, "->", qualities[i])

    max_quality = max(qualities)
    print("Max quality:", max_quality)


n = 20
population = generate_population(n)
qualities = evaluate_population(population)
display_pop_and_max_quality(qualities)
