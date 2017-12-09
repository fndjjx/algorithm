
class Node():

    def __init__(self, value=None, next_node=None):
        self._value = value
        self._next = next_node

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, next):
        self._next = next

if __name__=="__main__":
    node = Node()
    print(node.value)
    print(node.next)
    node.value=0
    print(node.value)
    n1 = Node(1)
    n2 = Node(2)
    n1.next=n2
    node.next=n1
    print(node.next)
    print(n1.next)
    

