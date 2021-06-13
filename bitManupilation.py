################################ Count setBits in an integer #######################################

def sbits(n):
    count = 0
    while(n):
        count += n&1
        n = n>>1    
    return count

##################  Find the two non-repeating elements in an array of repeating elements ############

def nRepEle(arr):
    sum = 0
    for i in range(len(arr)):
        sum = sum^arr[i]
    
    sum = sum & -sum
    num1= 0
    num2= 0

    for i in range(len(arr)):
        if arr[i]&sum == 0:
            num1 = num1^arr[i]
        else:
            num2= num2^arr[i]
    
    return("num1 :",num1 , "num2 :",num2)


########################  Count number of bits to be flipped to convert A to B  ########################


def bitFlip(a,b):
    N = a^b
    count = 0
    while(N):
        count+= N&1
        N >>= 1
    return count



##########################   Program to find whether a no is power of two  #################################

def powerOf2(N):
    if N == 0:
        return False
    if N&(N-1) == 0:
        return True
    else:
        return False



##########################  Count total set bits in all numbers from 1 to n  #########################

def allSetBits(N):
    if N <= 1:
        return N
    p2 = 0
    while((1<<p2) <= N):
        p2+=1
    p2 = p2-1
    SB = ((1<<(p2-1))*p2 )+ (N-(1<<p2)+1) + allSetBits(N-(1<<p2))
    return SB 


print(allSetBits(16))
