# q 1017 leet code

def negB2(n):
    if n == 0:
        return "0"

    ans = ""
    while n != 0:
        if abs(n%2) == 1:
            ans+="1"
            n = (n-1)/(-2)
        else:
            ans+="0"
            n = n/(-2)

    return ans[::-1]

print(negB2(7))
