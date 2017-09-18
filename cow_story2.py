'''
cow will give born to a litter cow each year, and litter cow will do the same after four years,
so when the nth year, how many cows in total?
'''
     

def cow_story(n):
    b=[1]
    s=[1]
    for i in range(1,n+1):
        if len(s)>3:
            b.append(b[-1]+s[-3]-s[-4])
            s.append(s[-1]+b[-1]-s[-3]+s[-4])
        elif len(s)==3:
            b.append(b[-1]+s[-3])
            s.append(s[-1]+b[-1]-s[-3])
        else:
            b.append(b[-1])
            s.append(s[-1]+b[-1])
        print(b)
        print(s)
    return b[-1]


if __name__=="__main__":
    for n in range(6):
        print("year{}".format(n+1))
        print(cow_story(n))

        
