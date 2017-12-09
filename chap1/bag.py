from node import Node

class Bag():
    def __init__(self):
        self.first = Node()
        self.last = self.first
        self.count = 0

    def add(self, value):
        node = Node(value)
        self.last.next = node
        self.last = node
        self.count += 1

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
        while current.next:
            current = current.next
            yield current.value


if __name__=="__main__":
    bag = Bag()
    bag.add(1)
    bag.add(2)
    bag.add(5)
    for i in bag.list_elements():
        print(i) 


    

