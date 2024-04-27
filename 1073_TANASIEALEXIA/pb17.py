#pb17
import numpy as np
def generate_individual(k):
    individual = np.random.choice([1, 2, 3, 4, 5, 6], size=k)

    while individual[-1] % 2 != 0:
        individual = np.random.choice([1, 2, 3, 4, 5, 6], size=k)
    quality = np.prod(individual)
    return individual, quality
k = 5

individuals = [generate_individual(k) for _ in range(10)]

sorted_individuals = sorted(individuals, key=lambda x: x[1])

print("sorted indiv")
for ind, qual in sorted_individuals:
    print(f"individ: {ind}, quality: {qual}")
