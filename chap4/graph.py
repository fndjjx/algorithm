import better_exceptions
import numpy as np
from collections import deque

class Graph():
    def __init__(self, l):
        self.adj = {}
        self.e = 0
        self.v = 0
        self.build_graph(l)

    def E(self):
        return self.e

    def V(self):
        return self.v

    def add_edge(self, v1, v2):
        if not v2 in self.adj[v1]:
            self.adj[v1].append(v2)
            self.adj[v2].append(v1)
            self.e += 1

    def build_graph(self, l):
        for i in l:
            if i[0] not in self.adj:
                self.adj[i[0]] = []
            if i[1] not in self.adj:
                self.adj[i[1]] = []
            self.add_edge(i[0],i[1])
        self.v = len(self.adj)

    def __str__(self):
        return str(self.adj)

class DFS():
    def __init__(self, graph):
        self.g = graph
        self.marked = []
        self._path = {}

    def dfs(self, start, end):
        s = self.g.adj[start]
        for i in s:
            self._path[i] = start
            self.marked.append(i)
            self._dfs(i, end)
        return self.path(start, end)

    def _dfs(self, v, end):
        for i in self.g.adj[v]:
            #self._path[i] = v
            if not i in self.marked:
                self._path[i] = v
                self.marked.append(i)
                self._dfs(i,end)

    def path(self, start, end):
        if not end in self._path:
            return None
        result = [end]
        v = end
        while v != start:
            result.append(self._path[v])
            v = self._path[v] 
        result = result[::-1]
        return result 

class BFS():
    def __init__(self, graph):
        self.g = graph
        self._path = {}

    def bfs(self, start, end):
        queue = deque()
        marked = []
        queue.append(start)
        while len(queue)!=0:
            v = queue.popleft()
            marked.append(v)
            for i in self.g.adj[v]:
                if not i in marked:
                    queue.append(i)
                    marked.append(i)
                    self._path[i] = v
        print(self._path)
        return self.path(start, end)

    def path(self, start, end):
        if not end in self._path:
            return None
        result = [end]
        v = end
        while v != start:
            result.append(self._path[v])
            v = self._path[v]
        result = result[::-1]
        return result
         

if __name__=="__main__":
    l=[[1,3],[0,1],[0,2]]
    l=[[0,1],[0,3],[1,0],[1,3],[1,4],[2,3],[2,4],[3,0],[3,1],[3,2],[3,4],[4,1],[4,2],[4,3]]
    l=[[0,1],[0,3],[2,3],[2,4]]
    g = Graph(l)
    print(g.E())
    print(g.V())
    print(g)
    d = DFS(g)
    print(d.dfs(1,4))
    b = BFS(g)
    print(b.bfs(1,4))
    
        
           
        

       

