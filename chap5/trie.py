import better_exceptions
from collections import OrderedDict

class Node:
    def __init__(self, char, val=None):
        self.char = char
        self.val = val
        self.children = OrderedDict()

    def add_child(self, child):
        if not child.char in self.children:
            self.children[child.char] = child
        self.children = OrderedDict(sorted([[k,v] for k,v in self.children.items()],key=lambda x:x[0]))

    def set_val(self, val):
        self.val = val

    def __str__(self):
        return "key: {}, val: {}".format(self.char, self.val)

class Trie():
    def __init__(self):
        self.root = Node(None)

    def add(self, key, val):
        self._add(self.root,key,val,0)

    def _add(self,current_node,key,val,depth):
        if depth+1==len(key):
            if not key[depth] in current_node.children:
                node = Node(key[depth], val)
                current_node.add_child(node)
            else:
                current_node.children[key[depth]].set_val(val)
        else:
            if not key[depth] in current_node.children:
                node = Node(key[depth])
                current_node.add_child(node)
            self._add(current_node.children[key[depth]],key,val,depth+1)

    def get(self, key):
        return self._get(self.root, key)

    def _get(self, current_node, key):
        char = key[0]
        key = key[1:]
        if not key:
            if char in current_node.children:
                return current_node.children[char].val
            else:
                return None
        else:
            if char in current_node.children:
                return self._get(current_node.children[char], key)
            else:
                return None

    def collect(self, prefix=None):
        result = []
        self._collect(self.root, result, "", prefix)
        return result

    def _collect(self, current_node, result, string, prefix):
        if current_node.char:
            string = string+current_node.char
        if current_node.val and ((prefix and string.startswith(prefix)) or (not prefix)):
            result.append(string)
        for next_char, next_node in current_node.children.items():
            self._collect(next_node, result, string, prefix)

    def delete(self, key):
        self._delete(self.root, key)

    def _delete(self, current_node, key):
        char = key[0]
        key = key[1:]
        if not key:
            if len(current_node.children[char].children)>0:
                current_node.children[char].val = None
            else:
                del current_node.children[char]
        else:
            self._delete(current_node.children[char], key)

        
        
        

    

if __name__=="__main__":
    l = [["string",1],["as",2],["sr",3],["str",10]]
    t = Trie()
    t.add("str",10)
    print(t.get("str"))
    t.add("string",1)
    t.add("str",20)
    print(t.get("str"))
    print(t.collect())
    for i in l:
        t.add(i[0], i[1])
    print(t.collect())
    print(t.get("string"))
    print(t.get("as"))
    print(t.get("sr"))
    print(t.get("stringg"))
    print(t.collect("a"))
    print(t.collect())
    t.delete("as")
    print(t.collect())
    t.delete("str")
    print(t.collect())
    t.add("str",1)
    print(t.collect())
    t.delete("string")
    print(t.collect())
        
        
        
