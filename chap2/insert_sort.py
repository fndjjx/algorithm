import better_exceptions

def insert_sort(l):
    for i in range(len(l)):
        for j in range(i-1):
            if l[i]<l[j]:
                l[i],l[j] = l[j], l[i]
        print(l)
    return l

if __name__=="__main__":
    a=[1,2,4,-1,2,10,11,45,34,2,0,0]
    print(insert_sort(a))
    aa=[1,2,4,-1,2,10,11,45,34,2,0,0]
    aa.sort()
    print(a==aa)
    
