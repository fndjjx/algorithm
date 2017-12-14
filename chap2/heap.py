import better_exceptions
import numpy as np

class heap():
    def __init__(self):
        self.heap = [None]
        self.count = 0

    def insert(self, v):
        self.count += 1
        self.heap.append(v) 
        self.swim(self.count)

    def swim(self, k):
        while k>1:
            if self.heap[int(k/2)]<self.heap[k]:
                self.heap[int(k/2)], self.heap[k] = self.heap[k], self.heap[int(k/2)]
            k = int(k/2)

    def sink(self, k):
        while k<=self.count/2:
            if self.count == 2*k: #预防只剩一个左子树
                if self.heap[k]<=self.heap[2*k]:
                    self.heap[2*k], self.heap[k] = self.heap[k], self.heap[2*k] 
                    k = 2*k
                else:
                    break
            elif self.heap[2*k]>self.heap[2*k+1]:#如果左子树大于右子树则和左边交换
                if self.heap[k]<=self.heap[2*k]:
                    self.heap[2*k], self.heap[k] = self.heap[k], self.heap[2*k] 
                    k = 2*k
                else:
                    break
            else:#如果右子树大于左子树则和右边交换
                if self.heap[k]<=self.heap[2*k+1]:
                    self.heap[2*k+1], self.heap[k] = self.heap[k], self.heap[2*k+1] 
                    k = 2*k+1
                else:
                    break

    def delMax(self):
        max_val = self.heap[1]
        self.heap[1], self.heap[self.count] = self.heap[self.count], self.heap[1]
        self.count -= 1
        self.heap.pop()
        self.sink(1)
        return max_val
         
    def show(self):
        s = ""
        count = 1
        for i in range(int(np.log2(self.count))+1):
            for j in range(2**i):
                if count>self.count:
                    break
                s += str(self.heap[count])
                s += " "
                count += 1
            s += "\n"
        return s

    def sort(self):
        result = []
        while self.count>=1:
            result.append(self.delMax())
       #     print(self.show())
        return result



if __name__=="__main__":
    h = heap()
    h.insert(10)
    h.insert(10)
    h.insert(1)
    print("before")
    print(h.show())
    print("max")
    print(h.delMax())
    print("after")
    print(h.show())

    a=[1,2,4,-1,2,10,11,45,34,2,0,0]
    h = heap()
    for i in a:
        h.insert(i)
    print(h.show())
    
    a = h.sort()
    print(a)
    aa=[1,2,4,-1,2,10,11,45,34,2,0,0]
    aa.sort(reverse=True)
    print(a==aa)
    


        
        
