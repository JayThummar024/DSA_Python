def waiter(number, q):
    # Write your code here
    primes = []
    a = number
    b = []
    x = 2
    ans = []
    
    while len(primes) < q:  
        if x > 1:  
            for i in range(2,x):  
                if (x % i) == 0:  
                    break  
            else:
                primes.append(x) 
        x+=1 
        

    for p in primes:
        temp = []
        for num in range(len(a)-1 , -1 ,-1):
            if a[num]%p == 0:
                b.append(a[num])
                temp+=[a[num]]
        print(a)
        print(b)

        a = a[::-1]
        
        for num in temp:
            a.remove(num)   

        ans = ans + b[::-1]
        b=[]

    ans = ans + a[::-1]

    return ans

print(waiter([3,3,4,4,9], 2))




                
    


