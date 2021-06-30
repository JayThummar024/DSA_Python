class Graph:
    def __init__(self , dict):
        self.graph_dict = dict
        print(self.graph_dict)

    def get_paths(self , start , end , path=[]):
        paths = []

        path = path + [start]

        if start == end:
            return [path]

        if len(self.graph_dict[start]) == 0:
            return []
        
        for node in self.graph_dict[start]:
           if node not in path:
                new_paths = self.get_paths(node, end ,path)
                for p in new_paths:
                    paths.append(p)
                
        return paths

    def shortest_path(self , start , end , path=[]):
        path = path + [start]

        if start == end:
            return path

        if len(self.graph_dict[start]) == 0:
            return None
        
        shortest_path = None

        for node in self.graph_dict[start]:
            if node not in path:
                sp = self.shortest_path(node, end , path)
                if sp:
                    if shortest_path is None or len(sp) < len(shortest_path):
                        shortest_path = sp
        
        return shortest_path

    def bfs(self , node ):
        visited = [False] * (max(self.graph_dict)+1)
        q = []

        visited[node] = True
        q.append(node)

        while q:
            x = q.pop(0)
            print (x, end = " ")
            for i in self.graph_dict[x]:
                if visited[i] == False:
                    q.append(i)
                    visited[i] = True


flights = {
    1:[2,3,4],
    2:[],
    3:[4,5],
    4:[2],
    5:[2,3]
}
  
routes = Graph(flights)
c=3
t=5
time=0
wait = 0
sp = routes.shortest_path(1,1)
print(sp)
x=t

if c > t:   
    while x<=c:
        x+=t
    wait = x-c
else:
    wait = t + (t-c)

roads = len(sp) - 1
station = roads - 1
tt = max(-1 , roads*c + station*wait)

print(tt)

