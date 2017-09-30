'''
http://blog.csdn.net/cc_again/article/details/25691925
'''

def fromul(i,j,a):
    if i==0 and j==0:
        return a[i][j]
    elif i==0 and j!=0:
        return a[i][j] + fromul(i,j-1,a)
    elif j==0 and i!=0:
        return a[i][j] + fromul(i-1,j,a)
    else:
        return a[i][j] + max(fromul(i-1,j,a), fromul(i,j-1,a))

def fromdl(i,j,a):
    if i==a.shape[0]-1 and j==0:
        return a[i][j]
    elif i==a.shape[0]-1 and j!=0:
        return a[i][j] + fromdl(i,j-1,a)
    elif j==0 and i!=a.shape[0]-1:
        return a[i][j] + fromdl(i+1,j,a)
    else:
        return a[i][j] + max(fromdl(i+1,j,a), fromdl(i,j-1,a))

def fromur(i,j,a):
    if i==0 and j==a.shape[1]-1:
        return a[i][j]
    elif i==0 and j!=a.shape[1]-1:
        return a[i][j] + fromur(i,j+1,a)
    elif j==a.shape[1]-1 and i!=0:
        return a[i][j] + fromur(i-1,j,a)
    else:
        return a[i][j] + max(fromur(i-1,j,a), fromur(i,j+1,a))

def fromdr(i,j,a):
    if i==a.shape[0]-1 and j==a.shape[1]-1:
        return a[i][j]
    elif i==a.shape[0]-1 and j!=a.shape[1]-1:
        return a[i][j] + fromdr(i,j+1,a)
    elif j==a.shape[1]-1 and i!=a.shape[0]-1:
        return a[i][j] + fromdr(i+1,j,a)
    else:
        return a[i][j] + max(fromdr(i+1,j,a), fromdr(i,j+1,a))

def max_path(a):
    r = []
    for i in range(a.shape[0]):
        for j in range(a.shape[1]):
            try:
                from_ul1 = fromul(i-1, j, a)+fromdr(i+1,j,a)
                from_dl1 = fromdl(i, j-1, a)+fromur(i,j+1,a)
                print(i,j)
                print(from_ul1)
                print(from_dl1)
                solution1 = from_ul1+from_dl1

                from_ul2 = fromul(i, j-1, a)+fromdr(i,j+1,a)
                from_dl2 = fromdl(i+1, j, a)+fromur(i-1,j,a)
                print(from_ul2)
                print(from_dl2)
                solution2 = from_ul2+from_dl2
                
                r.append(max(solution1, solution2))    
            except:
                pass 
    print(r)
    return max(r)
            

if __name__=="__main__":
    import numpy as np
    a=np.array([[100,100,100],[100,1,100],[100,100,100]])
    print(max_path(a))
