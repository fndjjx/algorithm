import better_exceptions
import numpy as np

class WeightedDigraph():
    def __init__(self):
        self.adj = {}
        self.E = []
        self.V =[]

    def add_edge(self, v1, v2, weight):
        self.V.append(v1)
        self.V.append(v2)
        self.V = list(set(self.V))
        if not v1 in self.adj:
            self.adj[v1] = []
        v1_ends = [i[0] for i in self.adj[v1]]
        if not v2 in v1_ends:
            self.adj[v1].append([v1,v2,weight])
            return [v1,v2,weight]
        else:
            return None

    def build_graph(self, l):
        for i in l:
            e = self.add_edge(i[0], i[1], i[2])
            if e:
                self.E.append(e)

    def __str__(self):
        return str(self.adj)

class Dijkstra():
    def __init__(self, graph):
        self.dist = {}
        self.path = {}
        self.g = graph
        self.s = []
        self.u = self.g.V.copy()

    def init(self, v):
        self.s.append(v)
        self.u.remove(v)
        ends = np.array([j[1] for j in self.g.adj[v]])
        weights = [j[2] for j in self.g.adj[v]]
        for i in self.g.V:
            if i in ends:
                self.dist[i] = weights[np.where(ends==i)[0][0]]
                self.path[i] = v
            elif i == v:
                self.dist[i] = 0
                self.path[i] = 0
            else:
                self.dist[i] = np.inf 
                self.path[i] = None

    def sp(self, v):
        self.init(v)
        print(self.dist)
        print(self.path)
        while len(self.u)>0:
            key = sorted([[k,v] for k,v in self.dist.items() if k not in self.s],key=lambda x:x[1])[0][0]
            self.s.append(key)
            self.u.remove(key)
            self.relax(key)

    def relax(self, v):
        if v in self.g.adj:
            for i in self.g.adj[v]:
                j = i[1]
                weight = i[2]
                if self.dist[j]>self.dist[v]+weight:
                    self.dist[j] = self.dist[v]+weight
                    self.path[j] = v

    def __str__(self):
        return "dist: {}\npath: {}".format(self.dist, self.path)
            

        
if __name__=="__main__":
    l = [[0,1,0.2],[0,3,0.3],[1,2,0.9],[1,4,0.6],[3,2,0.4],[4,2,0.1]]
    wdg = WeightedDigraph()
    wdg.build_graph(l)
    print(wdg)
    d = Dijkstra(wdg)
    d.sp(0)
    print(d)
