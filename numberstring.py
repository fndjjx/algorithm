'''
http://blog.csdn.net/cc_again/article/details/10858813
'''
import numpy as np


def solution(l):
    dp = np.zeros([len(l)+1,len(l)+2])
    dp[0,:] = 1
    print(dp)
    for i in range(1, len(l)+1):
        print("round",i)
        print(l[i-1])
        if l[i-1]=="l":
            for j in range(1, i+2):
                tmp = 0
                for k in range(1, j):
                    tmp+=dp[i-1][k]
                dp[i][j] = tmp
        elif l[i-1]=="d":
            for j in range(1, i+2):
                tmp = 0
                for k in range(j, i+1):
                    print(i-1, k)
                    tmp+=dp[i-1][k]
                dp[i][j] = tmp
        elif l[i-1]=="?":
            for j in range(1, i+2):
                tmp = 0
                for k in range(1, i+1):
                    tmp+=dp[i-1][k]
                dp[i][j] = tmp
        print(dp)
    return dp[-1]





if __name__=="__main__":
    l = ["?","?"]
    l = ["l","l"]
    l = ["l", "d"]
    l = ["d", "l"]
    l = ["?", "?"]
    l = ["?", "d"]
    print(solution(l))
