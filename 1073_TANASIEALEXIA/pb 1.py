#pb 1
import numpy as np
def f(x):
    return np.square(x[0]) - 2 * x[1] * x[2]
def generate_individuals(nr_individuals):
    individuals = np.zeros((nr_individuals, 4), dtype=float)
    for i in range(nr_individuals):
        valid_individual = False
        while not valid_individual:
            # verify x + y + z < 10
            x, y, z = np.random.uniform(-2, 7, 3)
            if x + y + z < 10:
                valid_individual = True
                individuals[i, :3] = [x, y, z]
        individuals[i, -1] = f(individuals[i, :3])
    return individuals
def find_max_individual(individuals):
    max_fitness = np.max(individuals[:, -1])
    max_individuals = individuals[individuals[:, -1] == max_fitness]
    return max_individuals
def main(nr_individuals=20):
    individuals = generate_individuals(nr_individuals)
    print("indiduals and their values")
    print(individuals)

    max_individuals = find_max_individual(individuals)
    print("\nthe best ind:")
    print(max_individuals)
if __name__ == "__main__":
    main()
