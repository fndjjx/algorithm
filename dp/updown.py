'''
http://blog.csdn.net/cc_again/article/details/9918313
'''
import scipy.special as ss
import numpy as np

def solution(l):
    dp = np.zeros([l+1,2])
    dp[0][0] = 1
    dp[0][1] = 1
    dp[1][0] = 1
    dp[1][1] = 1
    for i in range(2, l+1):
        ans = 0
        for j in range(1, i+1):
            ans += dp[j-1][0]*dp[i-j][1]*ss.comb(i-1,j-1)
        print(ans)
        dp[i][0]=dp[i][1]=ans/2
    return ans


if __name__=="__main__":
    l = 20
    print(solution(l))


