import numpy
def m_int_ra(x,pm,a,b):
    # operatorul de mutatie resetare aleatoare pentru intregi

    # I: x - individul supus mutatiei
    #    pm - probabilitatea de mutatie
    #    a, b - capete interval de definitie
    # E: y - individ rezultat
    #    da - 1 daca s-a produs mutatie, 0 daca y este chiar x

    y=x.copy()
    m=len(x)
    da=0
    for i in range(m):
        r=numpy.random.uniform(0,1)
        if r<pm:
            da=1
            y[i]=numpy.random.randint(a,b+1)
    return y, da

def s_ruleta_SUS(pop):
    # selectia tip ruleta multibrat

    # I: pop - bazinul de selectie
    # E: rez - populatia selectata

    m,n=numpy.shape(pop)
    p,q=d_FPS_ss(pop,2)                 #sau alta distributie
    rez=pop.copy()
    i=0
    k=0
    r=numpy.random.uniform(0,1/m)
    while k<m:
        while r<=q[i]:
            rez[k,:n]=pop[i,:n]
            r+=1/m
            k+=1
        i+=1
    return rez

def d_FPS_ss(pop,c):
    # distributia de selectie FPS cu sigma scalare

    # I: pop - bazinul de selectie
    #    c - constanta din formula de ajustare. uzual: 2
    # E: p - vector probabilitati de selectie individuale
    #    q - vector probabilitati de selectie cumulate

    m,n=numpy.shape(pop)
    medie=numpy.mean(pop[:,n-1])
    sigma=numpy.std(pop[:,n-1])
    val=medie-c*sigma
    g=[numpy.max([0, pop[i][n-1]-val]) for i in range(m)]
    s=numpy.sum(g)
    p=g/s
    q=[numpy.sum(p[:i+1]) for i in range(m)]
    return p,q

def r_unipunct(x,y,pr):
    # operatorul de recombinare unipunct

    # I: x, y - indivizi care se recombina
    #    pr - probabilitatea de recombinare
    # E: a, b - descendenti obtinuti
    #    da - 1 daca se creaza indivizi noi, 0 altfel

    a=x.copy()      #a=x[:]
    b=y.copy()
    da=0
    r=numpy.random.uniform(0,1)
    if r<pr:
        da=1
        m=len(x)
        poz=numpy.random.randint(m)
        a[poz:m]=y[poz:m]
        b[poz:m]=x[poz:m]
    return a, b, da