import better_exceptions

def merge(l, low, high, mid):
    ll = l.copy()
    i = low
    j = mid+1
    k = low
    while i<=mid or j<=high:
        if i>mid:
            l[k] = ll[j]
            j += 1
        elif j>high:
            l[k] = ll[i]
            i += 1
        elif ll[i]<ll[j]:
            l[k] = ll[i]
            i += 1
        else:
            l[k] = ll[j]
            j += 1
        k += 1

def merge_sort(l, low, high):
    if low<high:
        mid = low+int((high-low)/2)
        merge_sort(l, low, mid) 
        merge_sort(l, mid+1, high) 
        merge(l, low, high, mid) 

        
    
if __name__=="__main__":
    a=[1,2,4,-1,2,10,11,45,34,2,0,0]
    merge_sort(a, 0, len(a)-1)
    print(a)
    aa=[1,2,4,-1,2,10,11,45,34,2,0,0]
    aa.sort()
    print(a==aa)



