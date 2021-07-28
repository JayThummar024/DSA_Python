
k,l,m = map(int,input().split())

dp = [0]*1000005

dp[1] = 1
dp[l] = 1
dp[k] = 1
for i in range(1,100000):
    if i == l or i ==k: continue
    if dp[i-1] == 0: dp[i] = 1
    if i-k>0 and dp[i-k] == 0: dp[i] = 1
    if i-l>0 and dp[i-l] == 0: dp[i] = 1


queries = [i for i in map(int , input().split())]

for q in queries:
    if dp[q] == 1:
        print("A",end="")
    else:
        print("B",end="")
    