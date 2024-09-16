class BinarySearchTree:
    def __init__(self, value, depth = 1):
        self.value = value
        self.depth = depth
        self.left = None
        self.right = None
    
    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BinarySearchTree(value, self.depth + 1)
                print(f'Tree node {value} added to the left of {self.value} at depth {self.depth + 1}')
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BinarySearchTree(value, self.depth + 1)
                print(f'Tree node {value} added to the right of {self.value} at depth {self.depth + 1}')
            else:
                self.right.insert(value)
                
    def get_node_by_value(self, value):
        if value == self.value:
            return self
        elif value < self.value and self.left:
            return self.left.get_node_by_value(value)
        elif value > self.value and self.right:
            return self.right.get_node_by_value(value)
        else:
            return None


root = BinarySearchTree(100)
root.insert(50)
root.insert(125)
root.insert(75)
root.insert(25)

run1 = root.get_node_by_value(75)
print(run1.value)
run2 = root.get_node_by_value(55)
print(run2)