import better_exceptions
import numpy as np

class Node():
    def __init__(self, key=None, val=None, left=None, right=None):
        self.key = key
        self.val = val
        self.left = left
        self.right = right
    def __str__(self):
        return str(self.key)

class BST():
    def __init__(self):
        self.root = Node(-np.inf)
        self.count = 0
    
    def get(self, key):
        result = self._get(key, self.root)
        return result

    def _get(self, key, current_node):
        if not current_node:
            return None
        if current_node.key == key:
            return current_node.val
        elif current_node.key>key:
            return self._get(key, current_node.left)
        else:
            return self._get(key, current_node.right)

    def put(self, key, value):
        result = self._put(key, value, self.root)
        return result

    def _put(self, key, value, current_node):
        if not current_node:
            node = Node(key, value)
            self.count += 1
            return node
        if current_node.key == key:
            current_node.val = value
        elif current_node.key>key:
            current_node.left = self._put(key, value, current_node.left)
        else:
            current_node.right = self._put(key, value, current_node.right)
        return current_node

    def show(self):
        self._show(self.root)

    def _show(self, node):
        if node:
            print("{}, {}".format(node.key, node.val))
            self._show(node.left)
            self._show(node.right)

    def size(self):
        return self.count

    def min(self):
        return self._min(self.root.right)

    def _min(self, current_node):
        if not current_node.left:
            return current_node
        return self._min(current_node.left)

    def max(self):
        return self._max(self.root.right)

    def _max(self, current_node):
        if not current_node.right:
            return current_node
        return self._max(current_node.right)

    def deleteMin(self):
        self.root.right = self._deleteMin(self.root.right)

    def _deleteMin(self, current_node):
        if current_node.left == None: 
            return current_node.right
        else:
            current_node.left = self._deleteMin(current_node.left)
            return current_node

    def delete(self, key):
        self._delete(key, self.root.right)

    def _delete(self, key, current_node):
        if not current_node:
            return None
        if key>current_node.key:
            current_node.right = self._delete(key, current_node.right)
        elif key<current_node.key:
            current_node.left = self._delete(key, current_node.left)
        else:
            if not current_node.right:
                return current_node.left
            elif not current_node.left:
                return current_node.right
            else:
                node = self._min(current_node.right)
                node.right = self._deleteMin(current_node.right) 
                node.left = current_node.left
                return node
    
    def first_order(self):
        self._first_order(self.root.right)

    def _first_order(self, current_node):
        print(current_node.val)
        if current_node.left:
            self._first_order(current_node.left)
        if current_node.right:
            self._first_order(current_node.right)

    def middle_order(self):
        self._middle_order(self.root.right)

    def _middle_order(self, current_node):
        if current_node.left:
            self._middle_order(current_node.left)
        print(current_node.val)
        if current_node.right:
            self._middle_order(current_node.right)

    def last_order(self):
        self._last_order(self.root.right)

    def _last_order(self, current_node):
        if current_node.left:
            self._last_order(current_node.left)
        if current_node.right:
            self._last_order(current_node.right)
        print(current_node.val)
        
     
            
        
        
        
        
        
if __name__=="__main__":
    bst = BST()
    bst.put(2,20)
    bst.put(3,30)
    bst.put(1,10)
    bst.put(0.5,5)
    bst.put(2.5,25)
    bst.put(1.5,15)
    bst.put(4,40)
    bst.last_order()
    
