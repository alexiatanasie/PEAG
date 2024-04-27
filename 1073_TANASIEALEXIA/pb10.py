#pb10
import numpy as np
def f(a, x):
    if np.sum(x) > 0:
        return a * np.sum(x)
    else:
        return a * (-np.sum(x))


def gen(n, a):
    ind = np.zeros([n, 11], dtype="float")
    for i in range(n):
        ind[i, :11] = np.random.randint(-1, 2, 11)
        ind[i, -1] = f(a, ind[i, :11])
    return ind



def descrip(ind):
    qual = ind[:, -1]

    # Calcul medie
    mean_quality = np.mean(qual)
    print("Mean quality:", mean_quality)

    # Calcul deviație standard
    std_dev = np.std(qual)
    print("Standard deviation:", std_dev)

    # Calcul mediană
    median_quality = np.median(qual)
    print("Median quality:", median_quality)

    return mean_quality, std_dev, median_quality

def pb(n, a):

    ind = gen(n, a)  # Generate individuals
    print(ind)
    max_quality = np.max(ind[:, -1])  # Get maximum quality
    print("Max quality:", max_quality)

    mean_quality, std_dev, median_quality = descrip(ind)

print(pb(10, 5))