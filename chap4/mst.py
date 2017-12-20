import better_exceptions
from graph import Graph, DFS

class WeightedGraph():
    def __init__(self):
        self.adj = {}
        self.E = []

    def add_edge(self, v1, v2, weight):
        if not v1 in self.adj:
            self.adj[v1] = []
        if not v2 in self.adj:
            self.adj[v2] = []

        v1_ends = [i[0] for i in self.adj[v1]]
        v2_ends = [i[0] for i in self.adj[v2]]

        if not v2 in v1_ends:
            self.adj[v1].append([v2, weight])
            self.adj[v2].append([v1, weight])
            return [v1, v2, weight]
        else:
            return None

    def build_graph(self, l):
        for i in l:
            e = self.add_edge(i[0], i[1], i[2])
            if e:
                self.E.append(e)

    def __str__(self):
        return str(self.adj)

class Prim():
    def __init__(self, graph):
        self.g = graph
        self._path = []
        self.marked = []
        self.weights = []

    def prim(self, v):
        self.marked.append(v)
        self.weights.extend([[v,i[0],i[1]] for i in self.g.adj[v]])
        weights = []
        for i in self.weights:
            if not (i[0] in self.marked and i[1] in self.marked):
                weights.append(i)
        self.weights = weights
                 
        if len(self.weights)>0:
            self.weights.sort(key=lambda x:x[2])
            next_v = self.weights.pop(0)
            self._path.append([next_v[0],next_v[1]])
            if not next_v in self.marked:
                self.prim(next_v[1])

    def __str__(self):
        return str(self._path)

class Kruskal():
    def __init__(self, graph):
        self.g = graph
        self._path = []
        self.marked = []

    def __str__(self):
        return str(self._path)

    def kruskal(self):
        e_set = self.g.E
        e_set.sort(key=lambda x:x[2])
        for i in e_set:
            if not self.connected(i[0],i[1]):
                self._path.append([i[0],i[1]])
                self.marked.append(i[0])
                self.marked.append(i[1])

    def connected(self, v1, v2):
        if not v1 in self.marked or not v2 in self.marked:
            return False
        else:
            g = Graph(self._path)
            d = DFS(g)
            if d.dfs(v1,v2):
                return True
            else:
                return False
            
  
        
if __name__=="__main__":
    l = [[0,1,0.2],[0,3,0.3],[1,0,0.2],[1,2,0.9],[1,4,0.6],[2,1,0.9],[2,3,0.4],[2,4,0.1],[3,0,0.3],[3,2,0.4],[4,1,0.6],[4,2,0.1]]
    wg = WeightedGraph()
    wg.build_graph(l)
    print(wg)
    p = Prim(wg)
    p.prim(0)
    print(p)
    k = Kruskal(wg)
    k.kruskal()
    print(k)
    
