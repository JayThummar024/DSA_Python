mod = 1000000007
dp = [0]*100005

def flowers(k):
    global dp
    global mod
    dp[0] = 1

    for i in range(1,100005):
        if i < k:
            dp[i] = dp[i-1]
        else:
            dp[i] =( (dp[i-1]%mod) + (dp[i-k]%mod) )%mod

    for i in range(1,100005):
         dp[i] =( (dp[i-1]%mod) + (dp[i]%mod) )%mod

    return dp

t,k = map(int,input().split())

while t:
    a,b=map(int,input().split())
    flowers(k)
    print((dp[b] - dp[a-1]))
    dp = [0]*100005
    t-=1