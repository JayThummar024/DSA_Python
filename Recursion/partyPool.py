# given an integer n representing n person going to party , 
# every person can either go alone or in a pair , output the no of ways in which they can go to a party


def party(n):
    if n == 2:
        return 2
    if n == 1:
        return 1
    
    x = party(n-1) + (n-1)*party(n-2)
    return x


print(party(6))

# A B C
# A BC 
# AB C
# AC B