'''
http://blog.csdn.net/u010579068/article/details/49207347
'''

import numpy as np
def solution(l1, l2):
    dp = np.zeros([len(l1),len(l2)])
    for i in range(len(l1)):
        for j in range(len(l2)):
            if l1[i]==l2[j]:
                dp[i][j] = dp[i-1][j-1]+1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    print(dp)
    return dp[-1][-1]
         



if __name__=="__main__":
    l1 = "abcfbc"
    l2 = "abfcab"
    print(solution(l1,l2))
