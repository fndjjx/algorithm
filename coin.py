'''
http://acm.hdu.edu.cn/showproblem.php?pid=2844
'''
import numpy as np

def solution(l):
    m = l[0]
    dp=[]    
    for i in range(len(l[1])+1):
        tmp=[]
        for j in range(max(l[2])+1):
            tmp.append([])
        dp.append(tmp)
    
    dp[1][1] = [l[1][0]]
    for i in range(1, len(l[1])+1):
        if i==1:
            for j in range(2, l[2][i-1]+1):
                tmp = list(np.array(dp[i][j-1])+l[1][i-1])+dp[i][j-1]
                tmp.append(l[1][i-1])
                tmp = list(set(tmp))
                dp[i][j] = tmp
        else:
            for j in range(l[2][i-1]+1):
                if j==0:
                    dp[i][j] = dp[i-1][l[2][i-2]]
                else:
                    tmp = list(np.array(dp[i][j-1])+l[1][i-1])+dp[i][j-1]
                    tmp.append(l[1][i-1])
                    tmp = list(set(tmp))
                    dp[i][j] = tmp
    print(dp)
    r = list(filter(lambda x:x<=m, dp[-1][l[2][-1]]))
    return len(r)


if __name__=="__main__":
    l = [10,[1,2,4],[2,1,1]]
    #l = [5,[1,4],[2,1]]
    print(solution(l))
