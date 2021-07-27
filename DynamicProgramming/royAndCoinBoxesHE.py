
n = int(input())
m = int(input())

start = [0]*(n+5) 
end = [0]*(n+5)
temp = [0]*(n+5)
coins = [0]*(n+5)
while m:
    l ,r = map(int,input().split())
    start[l]+=1
    end[r]+=1
    m-=1

temp[1] = start[1]
for i in range(2,n+1):
    temp[i] = start[i] - end[i-1] + temp[i-1]

for j in range(n+1):
    coins[temp[j]]+=1

for k in range(n-1 ,-1,-1):
    coins[k] = coins[k] + coins[k+1]

q = int(input())

for i in range(q):
    x = int(input())
    print(coins[x])


