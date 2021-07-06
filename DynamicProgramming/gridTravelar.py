def gridTravelar(n,m,memo={}):
    key = str(n) + "," + str(m)
    if n==0 or m==0:
        return 0
    if n==1 and m==1:
        return 1
    if key in memo:
        return memo[key]

    memo[key] = gridTravelar(n-1, m,memo) + gridTravelar(n, m-1,memo)
    return memo[key]

print(gridTravelar(18, 18))