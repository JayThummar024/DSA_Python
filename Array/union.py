def doUnion(a,b):
    #code here
    U = []
    for i in range(len(a)):
        if a[i] in U:
            continue
        else:
            U.append(a[i])
    for i in range(len(b)):
        if b[i] in U:
            continue
        else:
            U.append(b[i])
    return(U)