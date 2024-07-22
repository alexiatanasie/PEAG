import numpy

def m_perm_schimb(x,pm):
    # operatorul de mutatie prin interschimbare pentru permutari

    # I: x - individul supus mutatiei
    #    pm - probabilitatea de mutatie
    # E: y - individul rezultat
    #    da - 1 daca s-a produs mutatie, 0 daca y este chiar x

    y=x.copy()
    r=numpy.random.uniform(0,1)
    da=0
    if r<pm:
        da=1
        m = len(x)
        p = numpy.random.randint(0, m, 2)
        while p[0] == p[1]:
            p[1] = numpy.random.randint(0,m)
        y[p[1]]=x[p[0]]
        y[p[0]]=x[p[1]]
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

def r_CX(x,y,pr):
    # operatorul de recombinare Cycle Crossover pentru permutari

    # I: x,y - cromozomii parinti
    #    pr - probabilitatea de recombinare
    # E: a,b - descendenti
    #    da - 1 daca se creaza indivizi noi, 0 altfel

    a=x.copy()
    b=y.copy()
    da = 0
    r=numpy.random.uniform(0,1)
    if r<pr:
        da = 1
        m=len(x)
        c,nrc=cicluri(x,y)
        for t in range(1,nrc+1,2):
            for i in range(m):
                if c[i]==t:
                    a[i]=y[i]
                    b[i]=x[i]
    return a, b, da

def cicluri(x,y):
    # determinare cicluri pentru CX

    # I: x, y - cromozomi
    # E: c - vector cu indicii ciclurilor
    #    cite - numarul de cicluri

    m=len(x)
    c=numpy.zeros(m,dtype=int)
    continua=1
    i=0
    cite=1
    while continua:
        a=y[i]
        c[i]=cite
        while x[i]!=a:
            j=list(x).index(a)
            c[j]=cite
            a=y[j]
        try:
            i=list(c).index(0)
            cite+=1
        except:
            continua=0
    return c,cite