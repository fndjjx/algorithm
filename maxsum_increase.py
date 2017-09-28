'''
http://acm.hdu.edu.cn/showproblem.php?pid=1087
'''
import numpy as np

def solution(l):
    dp = np.zeros(len(l))
    dp[0] = l[0]
    for i in range(1,len(l)):
        if l[i]<=l[i-1]:
            dp[i] = l[i]
        else:
            dp[i] = dp[i-1]+l[i]
    print(dp)
    return max(dp)



if __name__=="__main__":
    l = [1,3, 2]
    #l = [1, 2, 3, 4]
    #l = [3,3,2,1]
    print(solution(l))
