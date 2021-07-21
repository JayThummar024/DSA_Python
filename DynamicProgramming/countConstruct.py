def countConstruct(target , wordBank , memo={}):
    if target in memo:
        return memo[target]

    if target == "":
        return 1

    cnt = 0
    
    for word in wordBank:
        if target.startswith(word) == True:
            suffix = target[len(word):]
            restCnt = countConstruct(suffix, wordBank , memo)
            cnt += restCnt

    memo[target] = cnt
    return cnt




print(countConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", ["e","ee","eee","eeee","eeeeee"]))