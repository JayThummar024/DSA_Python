def pow(a,b):
    # return a**b
    if b == 0:
        return 1
    if b == 1:
        return a
    return a*pow(a,b-1)


def power(a,b):
    if b == 0: return 1
    if b==1: return a
    temp = power(a,int(b/2))
    if b%2==0: return temp * temp
    else: return a * temp * temp

print(power(2,10))

