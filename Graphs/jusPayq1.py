n,m,t,c = map(int,input("Enter n , m , t ,p separated with space : ").split())

graph = {}

for i in range(1 ,n+1):
    graph[i] = []

for i in range(m):
    s,e = map(int,input("Enter an edge : ").split())
    graph[s] += [e]
    graph[e] += [s]
print(graph) 

def shortest_p(graph , start , end , path=[]):
    path = path + [start]

    if start == end:
        return path

    if len(graph[start]) == 0:
        return None
    
    shortest_path = None

    for node in graph[start]:
        if node not in path:
            sp = shortest_p(graph ,node, end , path)
            if sp:
                if shortest_path is None or len(sp) < len(shortest_path):
                    shortest_path = sp
    
    return shortest_path

sp = sh_p(graph , 1 , n)









    

