# given an integer n representing n person going to party , 
# every person can either go alone or in a pair , output the no of ways in which they can go to a party


def party(n):
    if n == 1:
        return 1
    if n == 2:
        return 2

    return party(n-1) + party(n-1)*party(n-2)


print(party(3))

# A B C
# A BC 
# AB C
# AC B