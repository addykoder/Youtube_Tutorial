def lst(len):
    l=[]
    for i in range(len):
        l.append(i)
    return l

def bin(l,e):
    L=0
    U=len(l)-1
    E=(U+L)//2
    while U>=L:
        if l[E] == e:
            return E
        elif l[E] > e:
            U = E-1
            E = (U+L)//2
            continue
        elif l[E] < e:
            L = E+1
            E = (U + L) // 2
            continue

    return False



list = lst(10)

print(bin(list,0))

