# given an integer n , print all the number till n in lexicographical order

def lexico(n , i):
    if i > n: return
    print(i)
    for j in range(1 if i == 0 else 0,10): 
        lexico(n , (10*i) + j)

print(lexico(101, 0))


