import numpy as np

BUDGET = 5000
COST = np.array([100, 60, 50])
AUTONOMY = np.array([6000, 4200, 2800])
TCAS_RANGE = np.array([30, 48, 32])

def m_perm_inserare(x, pm):
    # Operator for permutation insertion mutation

    y = x.copy()
    r = np.random.uniform(0, 1)
    da = 0
    if r < pm:
        da = 1
        m = len(x)
        p = np.random.randint(0, m, 2)
        while p[0] == p[1]:
            p[1] = np.random.randint(0, m)
        p.sort()
        i = p[0]
        j = p[1]
        y[i + 2 : j + 1] = x[i + 1 : j]
        y[i + 1] = x[j]
    return y, da

def s_elitista(pop, desc):
    # Elitist selection of the next generation

    noua = desc.copy()
    dim, n = pop.shape
    max1 = np.max(pop[:, -1])
    i = np.argmax(pop[:, -1])
    max2 = np.max(desc[:, -1])
    if max1 > max2:
        k = np.argmin(desc[:, -1])
        noua[k, :] = pop[i, :]
    return noua

def s_turneu2(pop):
    # Tournament selection

    dim, m = pop.shape
    rez = np.zeros((dim, m))
    for i in range(dim):
        p = np.random.randint(0, dim, 2)
        if pop[p[0], -1] > pop[p[1], -1]:
            rez[i, :] = pop[p[0], :]
        else:
            rez[i, :] = pop[p[1], :]
    return rez

def r_unipunct(x, y, pr):
    # Single-point crossover operator

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

def generate_population(pop_size):

    population = []
    for _ in range(pop_size):
        chromosome = np.random.randint(0, BUDGET // COST.min() + 1, size=3)
        population.append(chromosome)
    return np.array(population)

def evaluate(chromosome):
    total_cost = np.sum(chromosome * COST)
    if np.sum(chromosome) == 0:
        return -1, -1, -1
    avg_autonomy = np.sum(chromosome * AUTONOMY) / np.sum(chromosome)
    avg_tcas_range = np.sum(chromosome * TCAS_RANGE) / np.sum(chromosome)
    return total_cost, avg_autonomy, avg_tcas_range

def genetic_algorithm(pop_size, generations, pr_crossover=0.8, pr_mutation=0.1):
    population = generate_population(pop_size)
    for generation in range(generations):
        fitness = [evaluate(chromosome) for chromosome in population]
        fitness = np.array(fitness)
        valid_indices = np.where((fitness[:, 0] <= BUDGET) & (fitness[:, 2] >= 40))[0]
        if len(valid_indices) > 0:
            population = population[valid_indices]
            fitness = fitness[valid_indices]
        else:
            continue
        population_with_fitness = np.hstack((population, fitness[:, 1].reshape(-1, 1)))
        parents = s_turneu2(population_with_fitness)
        crossover_children = []
        for i in range(0, len(parents), 2):
            if i + 1 < len(parents):
                child1, child2, da = r_unipunct(parents[i, :-1], parents[i + 1, :-1], pr_crossover)
                if da:
                    crossover_children.extend([child1, child2])
                else:
                    crossover_children.extend([parents[i, :-1], parents[i + 1, :-1]])
                    mutated_children = []
        for child in crossover_children:
            mutated_child, _ = m_perm_inserare(child, pr_mutation)
            mutated_children.append(mutated_child)
        mutated_children = np.array(mutated_children)
        new_fitness = [evaluate(chromosome) for chromosome in mutated_children]
        new_fitness = np.array(new_fitness)
        valid_indices = np.where((new_fitness[:, 0] <= BUDGET) & (new_fitness[:, 2] >= 40))[0]
        if len(valid_indices) > 0:
            mutated_children = mutated_children[valid_indices]
            new_fitness = new_fitness[valid_indices]
        mutated_children_with_fitness = np.hstack((mutated_children, new_fitness[:, 1].reshape(-1, 1)))
        population = s_elitista(population_with_fitness, mutated_children_with_fitness)

    best_solution = max(population, key=lambda ind: ind[-1])
    return best_solution

best_solution = genetic_algorithm(pop_size=100, generations=100)
print("Best solution:", best_solution)
