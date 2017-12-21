import better_exceptions


class KeySort():
    def sort(self, l):
        count = {}
        for i in l:
            if not i[1] in count:
                count[i[1]] = 1
            else: 
                count[i[1]] += 1
        cl = sorted([[k,v] for k,v in count.items()], key=lambda x:x[1], reverse=True)
        for i in range(len(cl)):
            if i==0:
                count[cl[i][0]] = 0
            else:
                count[cl[i][0]] = count[cl[i-1][0]] + cl[i-1][1]
        aux = [None]*len(l)
        for i in l:
            aux[count[i[1]]] = i
            count[i[1]] += 1
        return aux
            


if __name__=="__main__":
    l = [["ab",1],["ba",2],["ca",1],["da",3],["d",2]]
    k = KeySort()
    print(k.sort(l))
        
