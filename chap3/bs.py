import better_exceptions

def binary_search(l,low,high,v):
    mid = int((low+high)/2)
    if v==l[mid]:
        return mid
    elif v>l[mid]:
        return binary_search(l,mid+1,high,v)
    else:
        return binary_search(l,low,mid,v)

def binary_search2(l,v):
    low = 0
    high = len(l)-1
    while low<high:
        mid = int((low+high)/2)
        if l[mid] == v:
            return mid
        elif v>l[mid]:
            low = mid+1
        else:
            high = mid
            


if __name__=="__main__":
    a=[1,2,2,3,5,7,10]
    print(binary_search(a,0,len(a)-1,2))
    print(binary_search2(a,2))
