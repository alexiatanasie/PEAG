import numpy as np

def m_int_ra(x, pm, a, b):
    # operatorul de mutatie resetare aleatoare pentru intregi
    y = x.copy()
    m = len(x)
    da = 0
    for i in range(m):
        r = np.random.uniform(0, 1)
        if r < pm:
            da = 1
            y[i] = np.random.randint(a, b + 1)
    return y, da

def d_FPS_ss(pop, c):
    # distributia de selectie FPS cu sigma scalare
    m, n = np.shape(pop)
    medie = np.mean(pop[:, n - 1])
    sigma = np.std(pop[:, n - 1])
    val = medie - c * sigma
    g = [np.max([0, pop[i][n - 1] - val]) for i in range(m)]
    s = np.sum(g)
    p = g / s
    q = [np.sum(p[:i + 1]) for i in range(m)]
    return p, q

def s_ruleta_SUS(pop):
    # selectia tip ruleta multibrat

    # I: pop - bazinul de selectie
    # E: rez - populatia selectata

    if len(pop.shape) == 1:
        pop = pop.reshape(1, -1)  # Convert 1D array to 2D array with one row
    m, n = np.shape(pop)  # Get the dimensions of the population array
    p, q = d_FPS_ss(pop, 2)  # Calculate selection probabilities
    rez = pop.copy()
    i = 0
    k = 0
    r = np.random.uniform(0, 1 / m)
    while k < m:
        while r <= q[i]:
            rez[k] = pop[i]
            r += 1 / m
            k += 1
        i += 1
    return rez



def s_elitista(pop, desc):
    # selectia elitista a generatiei urmatoare
    noua = desc.copy()
    dim, n = np.shape(pop)
    max1 = max(pop[:, n - 1])
    i = np.argmax(pop[:, n - 1])
    max2 = max(desc[:, n - 1])
    if max1 > max2:
        k = np.argmin(desc[:, n - 1])
        noua[k, :] = pop[i, :]
    return noua

def r_unipunct(x, y, pr):
    # operatorul de recombinare unipunct
    a = x.copy()  # a=x[:]
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

def calculate_transport_cost(phenotype):
    # Calculate the total transport cost for a given phenotype
    total_cost = 0
    transport_cost = np.array([[0, 70, 50], [90, 60, 70], [0, 0, 100]])  # Transport cost matrix
    for i in range(len(phenotype)):
        for j in range(len(phenotype[i])):
            total_cost += phenotype[i][j] * transport_cost[i][j]
    return total_cost

def transportation_genetic_algorithm(population_size, num_generations, mutation_rate):
    # Genetic algorithm to solve the transportation problem

    def initialize_population():
        # Initialize the population with random solutions
        population = []
        for _ in range(population_size):
            solution = np.random.randint(0, 120, size=(3, 2))  # Randomly initialize amounts supplied
            population.append(solution)
        return population

    def fitness_function(solution):
        # Calculate the fitness of a solution (lower transport cost is better)
        phenotype = solution
        transport_cost = calculate_transport_cost(phenotype)
        return 1 / (1 + transport_cost)  # We use inverse of the cost as fitness

    def mutate_solution(solution):
        # Mutate a solution by randomly changing some elements
        mutated_solution = solution.copy()
        for i in range(len(mutated_solution)):
            for j in range(len(mutated_solution[i])):
                if np.random.rand() < mutation_rate:
                    mutated_solution[i][j] += np.random.randint(-5, 5)  # Small random change
                    mutated_solution[i][j] = max(0, mutated_solution[i][j])  # Ensure non-negative
        return mutated_solution

    def crossover(parent1, parent2):
        # Perform crossover to generate offspring
        crossover_point = np.random.randint(1, len(parent1))
        child1 = np.concatenate((parent1[:crossover_point], parent2[crossover_point:]))
        child2 = np.concatenate((parent2[:crossover_point], parent1[crossover_point:]))
        return child1, child2

    population = initialize_population()
    for _ in range(num_generations):
        fitness_values = [fitness_function(solution) for solution in population]
        new_population = []
        for _ in range(population_size // 2):
            parent1, parent2 = s_ruleta_SUS(population)
            child1, child2 = crossover(parent1, parent2)
            child1 = mutate_solution(child1)
            child2 = mutate_solution(child2)
            new_population.extend([child1, child2])
        population = s_elitista(population, new_population)

    best_solution = max(population, key=fitness_function)
    return best_solution

# Example usage
best_solution = transportation_genetic_algorithm(population_size=10, num_generations=100, mutation_rate=0.1)
print("Best solution:", best_solution)
