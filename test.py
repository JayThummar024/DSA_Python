# # def swapStr(s , i , j):
# #     x = s[i]
# #     y = s[j]
# #     s1 = s[0:i]
# #     s2 = s[i+1:j]
# #     s3 = s[j+1:]

# #     return s1 + y +s2 +x + s3


# # print(swapStr("JAY" ,0,2))
# n=3
# visited = [[False]*n]*n

# print(visited)
# visited[0][0] = True
# print(visited)

# cnt = 0

# def util(i):
#     global cnt
#     for j in range(0,i):
#         cnt+=1
#     return cnt

# print(util(5))
# print(cnt)

rows, cols = (5, 5)
 
# method 2a
arr = [[0]*cols]*rows
 
# lets change the first element of the
# first row to 1 and print the array
arr[0][0] = 1
 
for row in arr:
    print(row)
# method 2b
arr = [[0 for i in range(cols)] for j in range(rows)]
arr[0][0] = 1
for row in arr:
    print(row)
 
    




        
