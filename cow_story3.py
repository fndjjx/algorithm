'''
cow will give born to a litter cow each year, and litter cow will do the same after four years,
so when the nth year, how many cows in total?
'''
     

def cow_story(n):
    if n<3:
        return 1
    else:
        return cow_story(n-1)+cow_story(n-3)


if __name__=="__main__":
    for n in range(6):
        print("year{}".format(n+1))
        print(cow_story(n))

        
