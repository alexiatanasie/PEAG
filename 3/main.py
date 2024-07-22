import numpy as np

def r_multipunct(x, y, pr, n):
    # Multipoint crossover operator
    a = x.copy()
    b = y.copy()
    r = np.random.uniform(0, 1)
    if r < pr:
        m = len(x)
        p = np.random.choice(range(m), size=n, replace=False)
        p.sort()
        if n % 2 == 1:
            p = np.append(p, m)
        for i in range(0, n, 2):
            a[p[i]:p[i+1]] = y[p[i]:p[i+1]]
            b[p[i]:p[i+1]] = x[p[i]:p[i+1]]
    return a, b

def m_int_fluaj(x, pm, a, b, max):
    # Integer mutation operator using drift
    y = x.copy()
    m = len(x)
    for i in range(m):
        r = np.random.uniform(0, 1)
        if r < pm:
            f = np.random.randint(-max, max+1)
            y[i] = np.clip(y[i] + f, a, b)
    return y

def d_FPS_ss(pop,c):
    # distributia de selectie FPS cu sigma scalare
    m, n = np.shape(pop)
    medie = np.mean(pop[:, n-1])
    sigma = np.std(pop[:, n-1])
    val = medie - c * sigma
    g = [np.max([0, pop[i][n-1] - val]) for i in range(m)]
    s = np.sum(g)
    p = g / s
    q = [np.sum(p[:i+1]) for i in range(m)]
    return p, q

def s_ruleta_SUS(pop):
    # selectia tip ruleta multibrat
    m, n = np.shape(pop)
    p, q = d_FPS_ss(pop, 2)  # sau alta distributie
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

def s_elitista(pop, desc):
    # Elitist selection for the next generation
    noua = desc.copy()
    dim, n = np.shape(pop)
    max1 = np.max(pop[:, n-1])
    i = np.argmax(pop[:, n-1])
    max2 = np.max(desc[:, n-1])
    if max1 > max2:
        k = np.argmin(desc[:, n-1])
        noua[k, :] = pop[i, :]
    return noua

costs = np.array([1000, 800, 1500])
credits = np.array([5, 3, 8])
individual_study_hours = np.array([80, 40, 100])
available_budget = 10000

def initialize_population(population_size):
    return np.random.randint(0, available_budget // np.min(costs), size=(population_size, 3))

def evaluate(population):
    total_cost = np.sum(population * costs, axis=1)
    total_credits = np.sum(population * credits, axis=1)
    total_study_hours = np.sum(population * individual_study_hours, axis=1)
    penalty = np.where(total_study_hours > 70, total_study_hours - 70, 0)
    fitness = total_credits - penalty
    return fitness, total_cost

def genetic_algorithm(population_size, iterations):
    population = initialize_population(population_size)
    for _ in range(iterations):
        fitness, total_cost = evaluate(population)
        descendants = []
        for i in range(population_size // 2):
            a, b = r_multipunct(population[i], population[i+1], 0.8, 2)
            a = m_int_fluaj(a, 0.1, 0, available_budget // np.min(costs), 2)
            b = m_int_fluaj(b, 0.1, 0, available_budget // np.min(costs), 2)
            descendants.append(a)
            descendants.append(b)
        descendants = np.array(descendants)
        population = s_elitista(population, descendants)
    return population

final_population = genetic_algorithm(population_size=6, iterations=10)
print("Final population:")
print(final_population)
final_fitness, final_cost = evaluate(final_population)
print("Final fitness:", final_fitness)
print("Final cost:", final_cost)
