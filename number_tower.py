'''
find max path value for tree
    1
  1   10
30  1   2

the max valu path is 1-->1-->30 = 32


'''
class Node():
    def __init__(self, value, row, col):
        self.value = value
        self.row = row
        self.col = col
        self.__left_child = None
        self.__right_child = None

    @property
    def left_child(self):
        return self.__left_child

    @left_child.setter
    def left_child(self, value):
        self.__left_child = value


    @property
    def right_child(self):
        return self.__right_child

    @right_child.setter
    def right_child(self, value):
        self.__right_child = value

    def max_value(self, tree):
        if self.left_child == None:
            return self.value
        else:
            return self.value + max(tree.node(self.left_child).max_value(tree), tree.node(self.right_child).max_value(tree))

class Tree():
    def __init__(self, l):
        self.tree = []
        for row_index in range(len(l)):
            self.tree.append([])
            for col_index in range(len(l[row_index])):
                self.tree[row_index].append(None)

    def __str__(self):
        result = []
        for row in self.tree:
            tmp = []
            for col in row:
                tmp.append(col.value)
            result.append(tmp)
        return str(result)

    def node(self, location):
        return self.tree[location[0]][location[1]]

    def set_node(self, location, value):
        self.tree[location[0]][location[1]] = value

        

def build_tree(l):
    ''' l = [[1],[2,3],[4,5,6], [7,8,9,10]]
            1
          2   3
        4   5   6
      7   8   9   10
    '''
    tree = Tree(l)
    for row_index in range(len(l)):
        for col_index in range(len(l[row_index])):
            node = Node(l[row_index][col_index], row_index, col_index)
            if row_index+1<len(l):
                node.left_child = [row_index+1, col_index] 
                node.right_child = [row_index+1, col_index+1] 
            tree.set_node([row_index, col_index], node)
    return tree
            
     
if __name__=="__main__":
    
    l = [[1],[1,10],[30,5,6]]
    tree = build_tree(l)
    print(tree)
    print(tree.node([0,0]).max_value(tree))
