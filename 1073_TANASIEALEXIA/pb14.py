#pb14
import numpy as np

def calculate_quality(permutation):
    return sum(permutation[i] < i + 1 for i in range(len(permutation)))

def generate_permutations(n, k):
    permutations = []
    for _ in range(n):
        permutation = np.random.permutation(range(1, k+1))
        permutation[0] = 1  # P(1)=1
        permutation[-1] = k  # P(k) = k
        permutations.append(permutation)
    return permutations

def evaluate_permutations(permutations):
    return [calculate_quality(permutation) for permutation in permutations]

def display_results(permutations, qualities):
    print("Permutations and their qualities:")
    for i, permutation in enumerate(permutations):
        print(i+1, ":", permutation, "->", qualities[i])
    print("Max quality:", max(qualities))

n = 10
k = 8

permutations = generate_permutations(n, k)
qualities = evaluate_permutations(permutations)
display_results(permutations, qualities)