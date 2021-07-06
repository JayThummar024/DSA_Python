def isBalanced(s):
    # Write your code here
    stack = []
    dict = {
        ")" : "(",
        "}" : "{",
        "]" : "["
    }
    
    for i in range(len(s)):
        if s[i] not in dict:
            stack.append(s[i])
        elif len(stack) == 0:
            stack.append(s[i])
        elif stack[-1] == dict[s[i]]:
            stack.pop()
        elif stack[0] not in dict:
            return "NO"
        else:
            return "No"
       
            
    if len(stack)==0:
        return "YES"
    else:
        return "NO"

t = int(input())

for i in range(t):
    ip = input()
    print(isBalanced(ip))


