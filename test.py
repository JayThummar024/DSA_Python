def swapStr(s , i , j):
    x = s[i]
    y = s[j]
    s1 = s[0:i]
    s2 = s[i+1:j]
    s3 = s[j+1:]

    return s1 + y +s2 +x + s3


print(swapStr("JAY" ,0,2))




        
