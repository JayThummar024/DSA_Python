def canConstruct(target , wordBank , memo={}):
    if target in memo:
        return memo[target]

    if target == "":
        return True

    for word in wordBank:
        if target.startswith(word) == True:
            suffix = target[len(word):]
            
            if canConstruct(suffix, wordBank) == True:
                memo[suffix] = True
                return True
                
    memo[target] = False
    return False


w =["e","ee","eee","eeee","eeeee"]
print(canConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef",w ))


