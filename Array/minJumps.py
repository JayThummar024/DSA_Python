def minJumps(a):
    if len(a) == 1:
        return 0
    if a[0] == 0:
        return -1
    mi = a[0]
    step = a[0]
    jump = 1
    for i in range(1,len(a)):
        if i == len(a):
            return jump
        mi = max(mi , i+a[i])
        step-=1
        if step == 0:
            jump+=1
            if i < mi:
                return -1
            step = mi - i
    return -1