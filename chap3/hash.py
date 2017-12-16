import better_exceptions
import numpy as np


class chain():
    def __init__(self, m):
        self.m = m
        self.st = [[] for i in range(m)]

    def hashcode(self, key):
        return hash(key)%self.m

    def put(self, key, val):
        self.st[self.hashcode(key)].append([key, val])

    def get(self, key):
        l = self.st[self.hashcode(key)]
        for i in l:
            if i[0]==key:
                return i[1]
        return None

    def __str__(self):
        return str(self.st)



if __name__=="__main__":
    h = chain(3)
    h.put(0,10)
    h.put(1,20)
    h.put(2,30)
    h.put(3,40)
    print(h)
    print(h.get(3))
    
