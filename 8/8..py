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

