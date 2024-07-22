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
def s_elitista(pop,desc):
    # selectia elitista a generatiei urmatoare

    # I: pop - populatia curenta
    #    desc - descendentii populatiei curente
    # E: noua - matricea descendentilor selectati

    noua=desc.copy()
    dim,n=numpy.shape(pop)
    max1=max(pop[:,n-1])
    i=numpy.argmax(pop[:,n-1])
    max2=max(desc[:,n-1])
    if max1>max2:
        k=numpy.argmin(desc[:,n-1])
        noua[k,:]=pop[i,:]
    return noua
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