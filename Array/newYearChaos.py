def minimumBribes(a):
    # Write your code here
    ans = 0
    flag = False
    for i in range(len(a)):
        cnt = 0
        for j in range(i):
            if a[j] > a[i]:
                cnt+=1
        
        if a[i] - (i+1) - cnt > 2:
            print("Too chaotic")
            flag = True
            break
        
        ans+=cnt
     
    if flag == False:
        print(ans)



# approach 2

def minimumBribes(a):
    # Write your code here
    ans = 0
    for i in range(len(a)-1 , -1 ,-1):
        if a[i] != i+1:
            if i-1 >= 0 and q[i-1] == i+1:
                q[i-1] , q[i] = q[i] , q[i-1]
                ans+=1
            elif i-2 >= 0 and q[i-2] == i+1:
                q[i-2] = q[i-1]
                q[i-1] = q[i]
                q[i] = q[i-2]
                ans+=2
            else:
                print("Too chaotic")
                return           
                
    print(ans)