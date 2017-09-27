'''
http://acm.hdu.edu.cn/showproblem.php?pid=2602
'''
import numpy as np

def solution(l):
    volume = l[0]
    dp = np.zeros([len(l[1])+1, volume+1])
    dp[1][1] = 1
    for i in range(2, len(l[1])+1):
        for j in range(1, volume+1):
            if j-l[2][i-1]<0:
                tmp = 0
            else:
                tmp = dp[i-1][j-l[2][i-1]]+l[1][i-1]
            dp[i][j] = max(dp[i-1][j], tmp)
    print(dp)
    return dp[-1][-1]
    




if __name__=="__main__":
    l = [10,[1,2,3,4,5],[5,4,3,2,1]]
    print(solution(l))
