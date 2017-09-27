'''
http://acm.hdu.edu.cn/showproblem.php?pid=2159
'''

import numpy as np

def solution(l):
    need = l[0][0]
    tor = l[0][1]
    most_kill = l[0][2]
    
    dp = np.zeros([len(l[1])+1, tor+1]) 
    for i in range(1, len(l[1])+1):
        for j in range(1,tor+1):
            tmp=[]
            for k in range(int(j/l[2][i-1])+1):
                if j-k*l[2][i-1]<0:
                    tmp.append(0)
                else:
                    tmp.append(dp[i-1][int(j-k*l[2][i-1])]+k*l[1][i-1])
            dp[i][j] = max(tmp)
    print(dp)
    return dp[-1][-1]-need

def solution2(l):
    need = l[0][0]
    tor = l[0][1]
    most_kill = l[0][2]

    dp = np.zeros([tor+1])
    for i in range(1, len(l[1])+1):
        for j in range(tor, 0,-1):
            tmp=[0]
            for k in range(int(j/l[2][i-1])+1):
                tmp.append(dp[int(j-k*l[2][i-1])]+k*l[1][i-1])
            dp[j] = max(tmp)
    print(dp)
    return dp[-1]-need

def solution3(l):
    need = l[0][0]
    tor = l[0][1]
    most_kill = l[0][2]

    dp = np.zeros([tor+1, most_kill+1])
    for i in range(1, len(l[1])+1):
        for j in range(tor, 0, -1):
            for p in range(most_kill+1):
                tmp=[]
                for k in range(int(j/l[2][i-1])+1):
                    if k>p:
                        tmp.append(0)
                    else:
                        tmp.append(dp[int(j-k*l[2][i-1])][p-k]+k*l[1][i-1])
                dp[j][p] = max(tmp)
    print(dp)
    return dp[-1]-need


if __name__=="__main__":
    l = [[10,10,10],[1],[1]]
    #l = [[10,10,9],[1],[1]]
    #l = [[9,10,10],[1,2],[1,2]]
    print(solution3(l))
