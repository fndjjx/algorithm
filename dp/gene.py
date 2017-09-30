'''
http://poj.org/problem?id=1080
'''
import numpy as np
score = np.array([[5, -1, -2, -1, -3],  
    [-1, 5, -3, -2, -4],  
    [-2, -3, 5, -2, -2],  
    [-1, -2, -2, 5, -1],  
    [-3, -4, -2, -1, 0]])


m = {"A":0 ,"C":1, "G":2, "T":3, "-":4}

def solution(l1,l2):
    dp = np.zeros([len(l1)+1, len(l2)+1])
    dp[0][0] = 0
    for i in range(1, len(l2)+1):
        dp[0][i] = dp[0][i-1]+score[m["-"]][m[l2[i-1]]]
    for i in range(1, len(l1)+1):
        dp[i][0] = dp[i-1][0]+score[m[l1[i-1]]][m["-"]]

    for i in range(1, len(l1)+1):
        for j in range(1, len(l2)+1):
            dp[i][j] = max(dp[i-1][j-1]+score[m[l1[i-1]]][m[l2[j-1]]], dp[i-1][j]+score[m[l1[i-1]]][m["-"]], dp[i][j-1]+score[m["-"]][m[l2[j-1]]])
    print(dp)
        





if __name__=="__main__":
    l1 = "AGTGATG"
    l2 = "GTTAG"
    #l1 = "AGCTATT"
    #l2 = "AGCTTTAAA"
    print(solution(l1,l2))
