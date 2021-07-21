# given an integerr n , print all the binary strings which has no consecutive 1's

def binaryS(n , ans = "" , result=[]):
    if len(ans)==n:
        if ans not in result:
            result.append(ans)
        return

    if len(ans)>0:
        if ans[-1] == "0":
            binaryS(n , ans+"0" , result)
            binaryS(n , ans+"1" , result)
        else:
            binaryS(n , ans+"0" , result)
    else:
        binaryS(n , ans+"0" , result)
        binaryS(n , ans+"1" , result)
  
    return result

print(binaryS(2))