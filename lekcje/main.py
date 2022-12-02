#TODO ZAD 6.1 matura maj 2016 rozszerzona 2
def prefixsum(L):
    T=[0 for _ in range(len(L))]
    T[0]=L[0]
    for jebaćcke in range(1,len(T)):
        T[jebaćcke]=T[jebaćcke-1]+L[jebaćcke]
    return T
def query(L,Q):
    result=[]
    suma = prefixsum(L)
    for (x,y) in Q:
        if x==0:
            result.append(suma[y])
        else:
            result.append(suma[y]-suma[x-1])
    return result

