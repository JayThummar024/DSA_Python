def allConstruct(target , wordBank ):
    ans = []
    if target == "": return [[]]

    for word in wordBank:
        if target.startswith(word) == True:
            suffix = target[len(word):]
            suffixWays = allConstruct(suffix, wordBank)
            for way in suffixWays:
                way.insert(0,word)
            for way in suffixWays:
                ans.append(way)
    return ans


target = "potato"
wordBank = ["pot" ,"ato" , "potato" , "potat" , "o" , "p" ,"t"]            
print(allConstruct(target, wordBank))