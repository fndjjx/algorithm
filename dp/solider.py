'''
http://blog.csdn.net/cc_again/article/details/24841249
'''
import numpy as np
N = 3
M = 2
K = 2


def solution():
    def mostuv(u,v):
        #g at most u, r at most v
        dp = np.zeros([N+1, 3])
        dp[0][2]=1
        for i in range(1,N+1):
            last = dp[i-1][0] + dp[i-1][1] + dp[i-1][2]
            # for p
            dp[i][2] = last
            
            #for g
            if i<=u:
                dp[i][0]=last
            elif i==u+1:
                dp[i][0]=last-1
            else:
                dp[i][0]=last-dp[i-u-1][1]-dp[i-u-1][2]

            #for r
            if i<=v:
                dp[i][1]=last
            elif i==v+1:
                dp[i][1]=last-1
            else:
                dp[i][1]=last-dp[i-v-1][0]-dp[i-v-1][2]

        return sum(dp[-1])

    return mostuv(N, K)-mostuv(M-1, K)



        
      

def main():
    print(solution())


if __name__=="__main__":
    main()
