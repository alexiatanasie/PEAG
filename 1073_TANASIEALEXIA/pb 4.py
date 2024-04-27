#pb 4
import random
def quality_permutation(perm):

    quality = 0
    for i in range(len(perm)):
        for j in range(i + 1, len(perm)):
            if (perm[i] - perm[j]) % 2 == 0:
                quality += 1
    return quality

def generate_permutations(k, num_permutations):

    matrix = []
    for _ in range(num_permutations):
        perm = [random.randint(0, k-1) for _ in range(k)]
        quality = quality_permutation(perm)
        matrix.append(perm + [quality])
    return matrix

def max_quality(matrix):

    return max(row[-1] for row in matrix)


k = 5
num_permutations = 15
permutations_matrix = generate_permutations(k, num_permutations)
print("Matricea cu permutări și calități corespunzătoare:")
for row in permutations_matrix:
    print(row)
max_quality_value = max_quality(permutations_matrix)
print("Valoarea maximă a calității:", max_quality_value)
