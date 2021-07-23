# given a string of all unique char , print all the permutation of the string  


count = 0

def strPer(s , osf):  
    if s=="": 
        print(osf)
        global count
        count+=1
        return 

    for i in range(0,len(s)):
        strPer(s[0:i] +s[i+1:] , osf+s[i])



strPer("ABC", "")
print(count)

    

    