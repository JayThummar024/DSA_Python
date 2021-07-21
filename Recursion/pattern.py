# input 5
# * * * * *
# * * * *
# * * *
# * *
# *


def cone(n):
    if n < 1: return
    print("* "*n)
    cone(n-1)

# cone(5)

def cone1(n,i):
    if n<1: return
    if n > i:
        print("* " , end="")
        cone1(n,i+1)
    else:
        print()
        cone1(n-1,0)

# cone1(5 , 0)

def cone2(n,i=0):
    if n<1: return
    if n > i:
        cone2(n,i+1)
        print("* ",end="")
    else:
        cone2(n-1,0)
        print()
# cone2(5,0)

