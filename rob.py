'''
http://acm.hdu.edu.cn/showproblem.php?pid=2955
'''


import numpy as np
def solution(l):
    v = int(l[0]*10)
    items = l[1]
    items = [[i[0], int(i[1]*10)]for i in items]
#    print(items)
#    print(v)
    dp = np.zeros([len(items)+1, v+1])
    dp[1][1] = items[0][0]
    for i in range(1, len(items)+1):
        for j in range(1, v+1):
#            print(i, j)
            if j-items[i-1][1]<0:
                tmp=0
            else:
                tmp=dp[i-1][j-items[i-1][1]]+items[i-1][0]
            dp[i][j] = max(dp[i-1][j], tmp)
    print(dp)

    return dp[len(items)][v]



if __name__=="__main__":
    l1 = [0.4, [[1,0.2],[2,0.3],[3,0.5]]]
    l2 = [0.6, [[2,0.3],[2,0.3],[3,0.5]]]
    l3 = [1, [[1,0.3],[2,0.2],[3,0.5]]]
    l = [l1,l2,l3]
    print(solution(l3))
