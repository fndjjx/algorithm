def binary_search_recursion(l,n):
    def _binary_search(low, high, n):
        mid = int((low+high)/2)
        if low>high:
            return -1
        if n==l[mid]:
            return mid
        elif n>l[mid]:
            return _binary_search(mid+1, high, n)
        else:
            return _binary_search(low, mid, n)
    return _binary_search(0, len(l)-1, n)

def binary_search_not_recursion(l,n):
    low = 0
    high = len(l)-1
    while low<high:
        mid = int((low+high)/2)
        if n==l[mid]:
            return mid
        elif n>l[mid]:
            low = mid+1
        else:
            high = mid
    return -1

def binary_search_not_recursion_first_appear(l,n):
    low = 0
    high = len(l)-1
    while low<high:
        mid = int((low+high)/2)
        if l[mid]==n:
            while mid>0:
                mid -= 1
                if l[mid]!=n:
                    return mid+1
            return mid
        elif l[mid]>n:
            high = mid-1
        else:
            low = mid+1
    return -1

def binary_search_not_recursion_last_appear(l,n):
    low = 0
    high = len(l)-1
    while low<high:
        mid = int((low+high)/2)
        if l[mid]==n:
            while mid<len(l)-1:
                mid += 1
                if l[mid]!=n:
                    return mid-1
            return mid
        elif l[mid]>n:
            high = mid-1
        else:
            low = mid+1
    return -1


if __name__=="__main__":
    l = [1,2,2,3,4,4,4,5,6,7,7]
    n = 4
    print(binary_search_not_recursion_last_appear(l,n))
        
        
