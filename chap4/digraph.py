import better_exceptions
from collections import deque

class Digraph():
    def __init__(self):
        self.adj = {}
        self.e = 0

    def add_edge(self, v1, v2):
        if v2 not in self.adj[v1]:
            self.adj[v1].append(v2)
        self.e += 1

    def build_digraph(self, l):
        for i in l:
            if not i[0] in self.adj:
                self.adj[i[0]] = []
            self.add_edge(i[0],i[1])

    def __str__(self):
        return str(self.adj)

class DFS():
    def __init__(self, graph):
        self.g = graph
        self.marked = []
        self._path = {}

    def dfs(self, start, end):
        for i in self.g.adj[start]:
            self.marked.append(i)
            self._path[i] = start
            self._dfs(i)
        return self.path(start, end)

    def _dfs(self, v):
        if v in self.g.adj:
            for i in self.g.adj[v]:
                if not i in self.marked:
                    self.marked.append(i)
                    self._path[i] = v
                    self._dfs(i)

    def path(self, start, end):
        if not end in self._path:
            return None
        result = [end]
        v = end
        count = 0
        while v != start or count==0:
            result.append(self._path[v])
            v = self._path[v]
            count += 1
        result = result[::-1]
        return result

class BFS():
    def __init__(self, graph):
        self.g = graph
        self._path = {}

    def bfs(self, start, end):
        q = deque()
        marked = []
        q.append(start)
        while len(q)!=0:
            v = q.popleft()
            marked.append(v)
            if v in self.g.adj:
                for i in self.g.adj[v]:
                    if not i in marked:
                        marked.append(i)
                        q.append(i)
                        self._path[i] = v
        print(self._path)
        return self.path(start, end)

    def path(self, start, end):
        if not end in self._path:
            return None
        result = [end]
        v = end
        count = 0
        while v != start or count==0:
            result.append(self._path[v])
            v = self._path[v]
            count += 1
        result = result[::-1]
        return result

class Topo():
    def __init__(self, graph):
        self.g = graph
        self.marked = []
        self.pre = []
        self.post = []

    def dfs(self, v):
        self.pre.append(v)
        if v in self.g.adj:
            for i in self.g.adj[v]:
                if not i in self.marked:
                    self.marked.append(i)
                    self.dfs(i)
        self.post.append(v)

    def pre_order(self):
        return self.pre

    def post_order(self):
        return self.post

    def reverse_post_order(self):
        return self.post[::-1]


        
        
        


if __name__=="__main__":
    l=[[0,1],[0,2],[1,3],[2,1],[2,4]]
    dg = Digraph()
    dg.build_digraph(l)
    print(dg)
    mydfs = DFS(dg)
    print(mydfs.dfs(0,1))
    mybfs = BFS(dg)
    print(mybfs.bfs(0,1))
    mytopo = Topo(dg)
    mytopo.dfs(0)
    print(mytopo.pre_order())
    print(mytopo.post_order())
    print(mytopo.reverse_post_order())
    

    
       
