
dp = [[[-1 for i in range(2)] for j in range(105)] for k in range(105)]


def adjcBitCnt(n , k , f):
    global dp
    if n == 0:
        return 0

    if n == 1:
        if k == 0:
            return 1
        else:
            return 0

    if dp[n][k][f] != -1:
        return dp[n][k][f]

    remAns = -1

    if f == 0:
        remAns = adjcBitCnt(n-1, k, 0) + adjcBitCnt(n-1, k, 1)
    else:
        remAns = adjcBitCnt(n-1, k, 0) + adjcBitCnt(n-1, k-1, 1)

    dp[n][k][f] = remAns
    return dp[n][k][f]



p = int(input())

for i in range(p):
    d , n , k = map(int , input().split())
    ans = adjcBitCnt(n, k, 0)+adjcBitCnt(n, k, 1)
    print(d , ans)