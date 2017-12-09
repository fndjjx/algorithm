from node import Node
from exception import NotEnoughElementError
import better_exceptions

class Stack():
    def __init__(self):
        self.first = None
        self.count = 0

    def push(self, value):
        node = Node(value)
        node.next = self.first
        self.first = node
        self.count += 1

    def pop(self):
        if self.count<1:
            raise NotEnoughElementError
        else:
            value = self.first.value
            self.first = self.first.next
            self.count -= 1
            return value

    @property
    def size(self):
        return self.count

    @property
    def isEmpty(self):
        if self.count==0:
            return True
        else:
            return False

    def list_elements(self):
        current = self.first
        while current:
            value = current.value
            yield value
            current = current.next

if __name__=="__main__":
    s = Stack()
    s.push(1)
    s.push(1)
    s.push(2)
    for i in s.list_elements():
        print(i)
    s.pop()
    for i in s.list_elements():
        print(i)
    s.pop()
    for i in s.list_elements():
        print(i)
    s.pop()
    s.pop()
        
        
