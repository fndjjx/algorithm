'''
http://blog.csdn.net/cc_again/article/details/24844911
'''
N=6
K=2
import numpy as np

def solution():
    def mostu(u):
        #h at most u
        dp = np.zeros([N+1,2])
        dp[0][0]=1
        for i in range(1,N+1):
            last = dp[i-1][0]+dp[i-1][1]
            dp[i][0] = last
            #for h
            if i<=u:
                dp[i][1]=last
            elif i==u+1:
                dp[i][1]=last-1
            else:
                dp[i][1]=last-dp[i-u-1][0]

        print(dp)
        return np.sum(dp[-1])

    return 2**N-mostu(K-1)


if __name__=="__main__":
    print(solution())
        
