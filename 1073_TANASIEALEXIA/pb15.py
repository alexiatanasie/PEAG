import numpy as np

def generate_individuals(num_individuals):
    individuals = []
    for _ in range(num_individuals):
        binary_vector = np.zeros(9, dtype=int)
        indices = np.random.choice(9, size=5, replace=False)
        binary_vector[indices] = 1

        quality = sum(binary_vector)

        individuals.append((binary_vector, quality))
    return individuals

def display_ind_quality(individuals):
    print("Individuals and their qualities:")
    for i, (individual, quality) in enumerate(individuals):
        print(i+1, ":", individual, "->", quality)

num_individuals = 10
individuals = generate_individuals(num_individuals)
display_ind_quality(individuals)
