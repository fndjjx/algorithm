import better_exceptions

def shell_sort(l):
    h = 1
    while h<len(l)/3:
        h = 3*h+1

    while h>=1:
        for i in range(0, len(l), h):
            current_min = i
            for j in range(i, len(l), h):
                if l[j]<l[current_min]:
                    current_min = j
            l[i], l[current_min] = l[current_min], l[i]
        h = int(h/3)
    return l
    


if __name__=="__main__":
    a=[1,2,4,-1,2,10,11,45,34,2,0,0]
    print(shell_sort(a))
    aa=[1,2,4,-1,2,10,11,45,34,2,0,0]
    aa.sort()
    print(a==aa)



