'''
http://acm.hdu.edu.cn/showproblem.php?pid=1503
'''
import numpy as np

def solution(l1, l2):
    if l2[0] not in l1:
        l1, l2 = l2, l1
    dp = np.zeros([len(l1)+1,len(l2)+1])
    for i in range(1,len(l1)+1):
        for j in range(1,len(l2)+1):
            if l1[i-1]==l2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    print(dp)
    max_dp = dp[-1][-1]
    flag = False
    for i in range(len(l1)+1):
        for j in range(len(l2)+1):
            if dp[i][j] == max_dp:
                flag = True
                break
        if flag:
            break 
    print(j)
    new_str = l1 + l2[j:] 
    return new_str


if __name__=="__main__":
    l1 = "apple"
    l2 = "peach"
#    l1 = "pear" 
#    l2 = "peach"
#    l1 = "ananas" 
#    l2 = "banana"
    print(solution(l1,l2))
