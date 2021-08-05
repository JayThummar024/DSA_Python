

n , k , x = map(int , input().split())
freq = [0]*16
temp = [0]*16

arr = list(map(int , input().split()))

for i in range(len(arr)):
    freq[arr[i]] += 1

def jhonSnowCF(n,k,x):
    global temp
    global freq
    for j in range(k):
        for i in range(16):
            temp[i] = freq[i]
        parity = 0
        for i in range(16):
            if freq[i]>0:
                cur = i^x
                delta = freq[i]//2
                if parity == 0:
                    delta += (freq[i]&1)

                temp[i] -= delta
                temp[cur] += delta

                parity = parity^(freq[i]&1)

        for i in range(16):
            freq[i] = temp[i]


jhonSnowCF(n, k, x)
min_num = max(freq)
max_num = min(freq)

for i in range(len(freq)):
    if freq[i] >0:
        min_num = min(min_num , i)
        max_num = max(max_num , i)

print(max_num , min_num)




    


    

    