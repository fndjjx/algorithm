
import numpy as np
import math

def solution(l):
    vv = int(l[0]*100)
    items = l[1]
    new_items = []
    for i in items:
        count = 0
        d = {"a":0,"b":0,"c":0}
        for j in i:
            k = j[0]
            v = j[1]
            if k=="a":
                count += 1
                d["a"] += v
            elif k=="b":
                count += 1
                d["b"] += v
            elif k=="c":
                count += 1
                d["c"] += v
        if count == len(i) and d["a"]<=600 and d["b"]<=600 and d["c"]<=600 and sum(d.values())<=1000:
            new_items.append(sum(d.values()))
    print(new_items)

    dp = np.zeros([len(new_items)+1, vv+1])
    for i in range(1, len(new_items)+1):
        for j in range(1, vv+1): 
            if j-int(new_items[i-2]*100)<0:
                tmp=0
            else:
                tmp = dp[i-1][j-int(new_items[i-2]*100)]+new_items[i-2]
            dp[i][j] = max(dp[i][j-1], tmp)
    print(dp)
    return dp[-1][-1]
    


if __name__=="__main__":
    l= [1200.00, [[["x", 600], ["a",400]],[["c",200.5]],[["a",59.99], ["a",120.00], ["b",10.00]]]]
    #l= [200.00, [[["a", 23.5], ["b",100]],[["c",650]],[["a",59.99], ["a",120.00], ["x",10.00]]]]
    l= [1200.00, [[["a", 400], ["b",600]],[["c",200.5]]]]
    #l= [1200.50, [[["a", 400], ["b",600]],[["c",200.5]],[["a",100]]]]
    #l= [1320, [[["a", 500], ["b",500]],[["c",220]],[["a",100]], [["a",310]]]]
    print(l[1])
    print(solution(l))
