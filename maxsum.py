'''
http://acm.hdu.edu.cn/showproblem.php?pid=1003
'''

def solution(l):
    dp=[]
    for i in range(len(l)):
        dp.append([])
    dp[0] = [l[0], [0,0]]
    for i in range(1, len(l)):
        if dp[i-1][0]+l[i]>l[i]:
            dp[i] = [dp[i-1][0]+l[i], [dp[i-1][1][0], i]]
        else:
            dp[i] = [l[i], [i, i]]
    print(dp)
        
        


if __name__=="__main__":
    l = [6, -1, 5, 4, -7]
    #l =  [6,-1,5,4,-7]
    #l = [0, 6, -1, 1, -6, 7, -5]
    print(solution(l))
