from node import Node
from exception import NotEnoughElementError
import better_exceptions

class Queue():
    def __init__(self):
        self.first = None
        self.last = self.first
        self.count = 0
        
    def enqueue(self, value):
        node = Node(value)
        if self.count == 0 :
            self.first = node
        else:
            self.last.next = node
        self.last = self.first
        self.last = node
        self.count += 1

    def dequeue(self):
        if self.count > 1:
            value = self.first.value
            self.first = self.first.next
        elif self.count == 1:
            value = self.first.value
            self.first = None
            self.last = None
        else:
            raise NotEnoughElementError("Queue already empty")
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
             
        
if __name__ == "__main__":
    q = Queue()
    q.enqueue(1)
    q.enqueue(3)
    q.enqueue(2)
    for i in q.list_elements():
        print(i)
    q.dequeue()
    q.dequeue()
    q.dequeue()
    q.dequeue()
    for i in q.list_elements():
        print(i)

    
