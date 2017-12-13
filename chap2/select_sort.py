import better_exceptions

def select_sort(l):
    for i in range(len(l)):
        current_min = i
        for j in range(i+1, len(l)):
            if l[j]<l[current_min]:
                current_min = j
        print(l)
        l[i],l[current_min] = l[current_min],l[i]
        
    return l

if __name__=="__main__":
    a=[1,2,4,-1,2,10,11,45,34,2,0,0]
    print(select_sort(a))
        
