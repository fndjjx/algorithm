'''
http://blog.csdn.net/cc_again/article/details/11856847
'''
from numba import jit
import numpy as np

def get_min(l):
    maxl = max(l)
    for i in range(maxl+1):
        if i not in l:
            return i
    return maxl+1

def mex(l):
    dp=np.zeros(len(l))
    for i in range(len(l)):
        if i==0:
            dp[i] = get_min(l[:1])
            continue
        s = 0
        for j in range(i+1):
            t = l[j:i+1]
            s += get_min(t)
        dp[i] = dp[i-1]+s
        
    return dp[-1]



if __name__=="__main__":
    l = np.array([0,1,3])
    #l = []
    #for i in range(10):
    #    l.append(np.random.randint(10))
    print("l",l)
    print(mex(l))
