import numpy as np

# Recombination operator: one-point crossover
def r_unipunct(x, y, pr):
    a = x.copy()
    b = y.copy()
    da = 0
    r = np.random.uniform(0, 1)
    if r < pr:
        da = 1
        m = len(x)
        poz = np.random.randint(m)
        a[poz:m] = y[poz:m]
        b[poz:m] = x[poz:m]
    return a, b, da

# Mutation operator: swap mutation for permutations
def m_perm_schimb(x, pm):
    print("Content of x in m_perm_schimb:", x)
    y = x.copy()
    r = np.random.uniform(0, 1)
    da = 0
    if r < pm:
        da = 1
        m = len(x)
        p = np.random.randint(0, m, 2)
        while p[0] == p[1]:
            p[1] = np.random.randint(0, m)
        y[p[1]] = x[p[0]]
        y[p[0]] = x[p[1]]
    return y, da

# Fitness-proportional selection with sigma scaling
def d_FPS_ss(pop, c):
    m, n = np.shape(pop)
    medie = np.mean(pop[:, n-1])
    sigma = np.std(pop[:, n-1])
    val = medie - c * sigma
    g = [np.max([0, pop[i][n-1] - val]) for i in range(m)]
    s = np.sum(g)
    p = g / s
    q = [np.sum(p[:i+1]) for i in range(m)]
    return p, q

# Roulette wheel selection using stochastic universal sampling
def s_ruleta_SUS(pop):
    m, n = np.shape(pop)
    p, q = d_FPS_ss(pop, 2)
    rez = pop.copy()
    i = 0
    k = 0
    r = np.random.uniform(0, 1/m)
    while k < m:
        while r <= q[i]:
            rez[k, :n] = pop[i, :n]
            r += 1/m
            k += 1
        i += 1
    return rez

# Objective function
def objective_function(individual, distances):
    total_distance = 0
    for island in range(len(distances)):
        island_distances = [distances[island][warehouse] for warehouse in individual]
        total_distance += min(island_distances)
    return total_distance

# Genetic algorithm
def genetic_algorithm_custom(num_islands, distances, population_size=100, num_generations=100, pr=0.8, pm=0.1):
    # Initialize population
    population = np.array([np.random.choice(range(num_islands), size=3, replace=False) for _ in range(population_size)])

    # Genetic algorithm
    def genetic_algorithm_custom(num_islands, distances, population_size=100, num_generations=100, pr=0.8, pm=0.1):
        # Initialize population
        population = np.array(
            [np.random.choice(range(num_islands), size=3, replace=False) for _ in range(population_size)])

        # Evolution loop
        for generation in range(num_generations):
            # Parent Selection
            selected_parents = [s_ruleta_SUS(population) for _ in range(population_size // 2)]

            # Crossover
            offspring = [r_unipunct(parent1, parent2, pr) for parent1, parent2 in
                         zip(selected_parents[::2], selected_parents[1::2])]
            offspring = [child for pair in offspring for child in pair[:2]]  # Flatten the list

            # Mutation
            mutated_offspring = [m_perm_schimb(child, pm) for child in offspring]

            # Elitist Selection
            population = np.array([min(mutated_offspring, key=lambda x: objective_function(x, distances))])

        # Return and print the best individual
        best_individual = min(population, key=lambda x: objective_function(x, distances))
        best_distance = objective_function(best_individual, distances)
        print("Best solution:", best_individual)
        print("Best distance:", best_distance)
        return best_individual, best_distance