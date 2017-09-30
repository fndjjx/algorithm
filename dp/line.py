'''
http://acm.hdu.edu.cn/showproblem.php?pid=2050
'''

def line(n):
    if n==1:
        return 2
    elif n==2:
        return 4
    else:
        return (n-2) + 2 + line(n-1)

def fold_line(n):
    if n==1:
        return 2
    else:
        return (2*(n-1)-1) + 2 +  (2*n-1-2) + 1 + fold_line(n-1)



if __name__=="__main__":
    for i in range(1, 10):
        #print(line(i))
        print(fold_line(i))
