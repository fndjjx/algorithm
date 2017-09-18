'''
cow will give born to a litter cow each year, and litter cow will do the same after four years,
so when the nth year, how many cows in total?
'''

class Cow():
    def __init__(self, state="s"):
        self.state = state
        self.t = 1

    def grow(self):
        if self.t<3:
            self.t += 1
        else:
            self.state = "b"

    def give_born(self):
        if self.state == "b":
            return Cow()

    def __repr__(self):
        return self.state


class Horde():
    def __init__(self):
        self.horde = [Cow("b"),Cow()]

    def pass_one_year(self):
        for i in self.horde:
            i.grow()
        for i in self.horde:
            new_cow = i.give_born()
            if new_cow:
                self.horde.append(new_cow)

    def pass_n_years(self, n):
         
        for i in range(n):
            self.pass_one_year()
            print(self.horde)

        return len(self.horde)

    def __str__(self):
        return str([str(i) for i in self.horde])
       

if __name__=="__main__":
    for n in range(6):
        h = Horde()
        print("year{}".format(n+1))
        print(h.pass_n_years(n))
       # print(h)
     

        
