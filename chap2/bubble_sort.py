import better_exceptions

def bubble_sort(l):
    for i in range(len(l)):
        for j in range(len(l)-1,i,-1):
            if l[j]<l[j-1]:
                l[j],l[j-1] = l[j-1],l[j]
    

if __name__=="__main__":
    a=[1,2,4,-1,2,10,11,45,34,2,0,0]
    bubble_sort(a)
    print(a)
    aa=[1,2,4,-1,2,10,11,45,34,2,0,0]
    aa.sort()
    print(a==aa)

   
