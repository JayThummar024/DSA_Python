def combinationSum(target , arr , memo={}):
    if target in memo:
        return memo[target]
        
    if target == 0 :
        return []

    if target < 0:
        return None

    for num in arr:
        remainder = target - num
        remResult = combinationSum(remainder, arr , memo)
        if remResult:
            remResult.append(num)   
            memo[remainder] = remResult
            return remResult
        
    memo[target] = None
    return None

print(combinationSum(9, [3,1]))