def strPer2(s , j):
    if j == len(s)-1:
        print("".join(s))
        return
    
    for i in range(j,len(s)):
        s[i] , s[j] = s[j] ,s[i]
        strPer2(s, j+1)
        s[i] , s[j] = s[j] ,s[i]


strPer2(list("ABC"), 0)