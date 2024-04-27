import numpy as np

def calculate_quality(permutation):
    quality = 0
    for i in range(len(permutation)-1):
        if permutation[i] == i+1 and permutation[i+1] == i+2:
            quality=quality+1
    return quality

def generate_permutations(n):
    permutations = []
    for _ in range(n):
        permutation = np.random.permutation(7) + 1  #generate permutations of size 7
        permutations.append(permutation)
    return permutations

def evaluate_permutations(permutations):
    qualities = [calculate_quality(perm) for perm in permutations]
    return qualities

def display_permutations_and_qualities(permutations, qualities):
   print("Generated individuals and their qualities:")
   for i,permutation in enumerate(permutations):
       print(i+1, ":", permutation, "->", qualities[i])

def display_max_quality(qualities):
    max_quality = max(qualities)
    print("Max quality:", max_quality)

n = 10
permutations = generate_permutations(n)
qualities = evaluate_permutations(permutations)
display_permutations_and_qualities(permutations, qualities)
display_max_quality(qualities)