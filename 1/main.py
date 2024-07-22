import numpy as np

def r_OCX(x, y, pr):
    # Operatorul de recombinare Order Crossover pentru indivizi permutări

    # I: x, y - indivizi care se recombină (permutări)
    #    pr - probabilitatea de recombinare
    # E: a, b - descendenți obținuți
    #    da - 1 dacă se creează indivizi noi, 0 altfel

    a = x[:]
    b = y[:]
    da = 0
    r = np.random.uniform(0, 1)
    if r < pr:
        da = 1
        m = len(x)
        p = np.random.randint(0, m, 2)
        while p[0] == p[1]:
            p[1] = np.random.randint(m)
        p.sort()
        a = OCX(x, y, p)
        b = OCX(y, x, p)
    return a, b, da

def OCX(x, y, p):
    # Generarea unui descendent conform Order Crossover

    # I: x, y - părinți
    #    p - vector cu cele 2 poziții
    # E: d - descendentul creat

    m = len(x)
    d = np.zeros(m, dtype=int) - 1
    d[p[0]:p[1] + 1] = x[p[0]:p[1] + 1]
    unde = p[1] + 1
    for i in [k for k in range(p[1], m)] + [k for k in range(p[1])]:
        if not (y[i] in d):
            if unde >= m:
                unde = 0
            d[unde] = y[i]
            unde += 1
    return d

def m_perm_schimb(x, pm):
    # Operatorul de mutație prin interschimbare pentru permutări

    # I: x - individul supus mutației
    #    pm - probabilitatea de mutație
    # E: y - individul rezultat
    #    da - 1 dacă s-a produs mutație, 0 dacă y este chiar x

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
def s_turneu(population, k, nr):
    dim = len(population)
    rez = [[] for _ in range(nr)]
    for i in range(nr):
        tournament = [population[np.random.randint(0, dim)] for _ in range(k)]
        valori = [evaluate_solution(individual, conflict_matrix) for individual in tournament]
        cine = np.argmax(valori)
        rez[i] = tournament[cine]
    return rez

def s_elitista(pop,desc):
    # selectia elitista a generatiei urmatoare

    # I: pop - populatia curenta
    #    desc - descendentii populatiei curente
    # E: noua - matricea descendentilor selectati

    noua=desc.copy()
    dim,n=np.shape(pop)
    max1=max(pop[:,n-1])
    i=np.argmax(pop[:,n-1])
    max2=max(desc[:,n-1])
    if max1>max2:
        k=np.argmin(desc[:,n-1])
        noua[k,:]=pop[i,:]
    return noua
def generate_pop_init(N, nr_cities):
    population = []
    for _ in range(N):
        solution = np.random.permutation(nr_cities)
        population.append(solution)
    return population

def generate_offspring(parents, mutation_rate, conflict_matrix):
    offspring = []
    num_parents = len(parents)
    for i in range(0, num_parents, 2):
        parent1 = parents[i]
        parent2 = parents[i + 1]
        child1, child2, _ = r_OCX(parent1, parent2, 0.8)
        child1, _ = m_perm_schimb(child1, mutation_rate)
        child2, _ = m_perm_schimb(child2, mutation_rate)
        offspring.append(child1)
        offspring.append(child2)
    return offspring

def evaluate_solution(solution, conflict_matrix):
    score = 0
    num_cities = len(solution)
    for i in range(num_cities):
        city1 = solution[i]
        city2 = solution[(i + 1) % num_cities]
        score += conflict_matrix[city1][city2]
    return score

def genetic_algorithm(N, num_cities, conflict_matrix, mutation_rate, max_generations):

    population = generate_pop_init(N, num_cities)
    for generation in range(max_generations):
        parents = s_turneu(population, 3, N)
        population = generate_offspring(parents, mutation_rate, conflict_matrix)
        best_solution = min(population, key=lambda x: evaluate_solution(x, conflict_matrix))
        best_score = evaluate_solution(best_solution, conflict_matrix)
        print(f"Generation {generation + 1}: Best score = {best_score}")
        if best_score == 0:
            break
    return best_solution

N = 50
num_cities = 10
mutation_rate = 0.1
max_generations = 10

conflict_matrix = np.random.randint(2, size=(num_cities, num_cities))

best_solution = genetic_algorithm(N, num_cities, conflict_matrix, mutation_rate, max_generations)
print("Best seating arrangement:", best_solution)
