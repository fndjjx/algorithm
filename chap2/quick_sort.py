import better_exceptions

def partition(l,low,high):
    i = low
    j = high
    v = l[low]
    print(v)
    while True:
        while i<j:
            if v>l[j]: 
                break
            else:
                j -= 1
        while i<j:
            if v<=l[i]:
                break
            else:
                i += 1
        if i>=j:
            break
        l[i],l[j] = l[j], l[i]
        
    l[low], l[j] = l[j], l[low]
    return i

def quick_sort(l, low, high):
    if low<high:
        k = partition(l, low, high)
        print(k)
        print(l)
        quick_sort(l,low,k)
        quick_sort(l,k+1,high)

if __name__=="__main__":
    a=[1,2,4,-1,2,10,11,45,34,2,0,0]
    quick_sort(a, 0, len(a)-1)
    print(a)
    aa=[1,2,4,-1,2,10,11,45,34,2,0,0]
    aa.sort()
    print(a==aa)        

