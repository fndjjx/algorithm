import better_exceptions

class LSD():
    def sort(self, l):
        bit_num = len(l[0])
        for b in range(bit_num-1,-1,-1):
            count = {}
            for i in l:
                if not ord(i[b]) in count:
                    count[ord(i[b])] = 1
                else:
                    count[ord(i[b])] += 1
            cl = sorted([[k,v] for k,v in count.items()],key=lambda x:x[0])
            for i in range(len(cl)):
                if i==0:
                    count[cl[i][0]] = 0
                else:
                    count[cl[i][0]] = count[cl[i-1][0]] + cl[i-1][1]
            aux = [None]*len(l)
            for i in l:
                aux[count[ord(i[b])]] = i
                count[ord(i[b])] += 1

            l = aux
            print(l)
                
          

        

if __name__=="__main__":
    l = ["abs","bfs","lpo","abs","lpo","asa"]
    #l = ["a","a","d","v","l","s"]
    lsd = LSD()
    lsd.sort(l)
