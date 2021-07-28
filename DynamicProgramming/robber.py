# given n houses containing gold , if a robber tries to loot the gold and wants to maximize the robbed amount,
# but he cant rob the two consicutive houses, maximize the robbed amount

def robber(dp , n):
    if n == 1: return dp[0]
    if n == 2: return max(dp[1],dp[0])

    for i in range(2,n):
        dp[i] = max(dp[i]+dp[i-2] , dp[i-1])

    print(dp)
    return dp[n-1]


dp = [1,8,4,2,1,4]
print(robber(dp,len(dp)))