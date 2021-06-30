# Factorial of a number

def factorial(n):
    if n >= 0 and int(n) == n:
        if n <= 0:
            return 1
        else:
            return n*factorial(n-1)
            n = n-1
    else:
        return "number must br positive integer"


print(factorial(5))

# fibonacci number at a given place


def fibonacci(n):
    if n >= 0 and int(n) == n:
        if n in [0, 1]:
            return n
        else:
            return fibonacci((n-1)) + fibonacci((n-2))
    else:
        return "number must br positive integer"


print(fibonacci(9))

# sum of digits of a given number


def summOfDigits(n):
    if n >= 0 and int(n) == n:
        if n == 0:
            return 0
        else:
            return int(n % 10) + summOfDigits(int(n/10))
    else:
        return "number must br positive integer"


print(summOfDigits(24563))

# power of number using recursion


def powerOfNum(num, pow):
    if pow < 0:
        return "power must br positive integer"

    else:
        if pow == 0:
            return 1
        else:    
            return num*powerOfNum(num,pow-1)


print(powerOfNum(-1.5,3))

# decimal to binary conversion

def dtb(n):
    if n == 0:
        return 0
    else:
        return n%2 + 10*(dtb(int(n/2)))  

print(dtb(10))  


# GCD of two numbers by Eucledian algorithm

def gcd(a,b):
    assert int(a)==a and int(b)==b , "The numbers must be an integers"
    if a<0:
        a=-1*a
    if b<0:
        b=-1*b    
    if b==0:
        return a
    else:        
        return gcd(b,a%b)

print(gcd(-4,-18))