'''
    m level stairs, you can step one or two once, how many different paths?
'''

def paths(n):
    if n==1:
        return 1
    elif n==2:
        return 2
    else:
        return paths(n-1) + paths(n-2)


if __name__=="__main__":
    print(paths(4))
