#pb19
import numpy as np

def calculate_quality(permutation):
    quality = sum(i for i, val in enumerate(permutation) if val % 2 == 0)
    return quality

def generate_permutations(n):
    permutations = []
    for _ in range(n):
        permutation = np.random.permutation(6)
        while 1 in permutation[:3]:
            permutation = np.random.permutation(6)
        permutations.append(permutation)
    return permutations

def evaluate_permutations(permutations):
    qualities = [calculate_quality(perm) for perm in permutations]
    return qualities

def display_max_quality(qualities):
    max_quality = max(qualities)
    print("Max quality:", max_quality)

n = 10
permutations = generate_permutations(n)

qualities = evaluate_permutations(permutations)

display_max_quality(qualities)
