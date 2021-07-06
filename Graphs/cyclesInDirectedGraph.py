graph = {
    0 : [1,2],
    1 : [],
    2 : [3],
    3 : []
}

def isCyclic(graph , node):
    visited = [False] * (max(graph)+1)
    recStack = [False] * (max(graph)+1)
    s = []

    s.append(node)
    recStack[node] = True
    while s:
        temp = s.pop()
        visited[temp] = True
        recStack[temp] = True

        for nieghbour in graph[temp]:
            if visited[nieghbour] == False:
                s.append(nieghbour)
            if recStack[nieghbour] == True:
                return True

        recStack[temp] == False
    return False

print(isCyclic(graph, 0))
