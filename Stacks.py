from node import Node

class Stack:
    def __init__(self):
        self.top_item = None
    
    def peek(self):
        return self.top_item.get_value()
    
    def push(self, value):
        self.item = Node(value)
        self.item.set_next_node(self.top_item)
        self.top_item = self.item