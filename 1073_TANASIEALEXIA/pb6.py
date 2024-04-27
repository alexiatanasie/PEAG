#pb6
import numpy as np

def quality_permutation(perm):
    quality = 0
    for i in range(len(perm)):
        for j in range(i + 1, len(perm)):
            if perm[i] == j and perm[j] == i:
                quality += 1
    return quality

def generate_permutations(n):

    permutations_matrix = np.zeros((n, 9), dtype=int)
    for i in range(n):
        perm = np.random.permutation(8)
        quality = quality_permutation(perm)
        permutations_matrix[i, :8] = perm
        permutations_matrix[i, -1] = quality
    return permutations_matrix

def max_quality(matrix):

    return np.max(matrix[:, -1])

n = 10
permutations_matrix = generate_permutations(n)
print("matrix :")
print(permutations_matrix)
max_quality_value = max_quality(permutations_matrix)
print("the max quality val:", max_quality_value)
