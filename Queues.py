from Nodes import Node
from Nodes import DoublyLinkedList
dll = DoublyLinkedList()
class Queue:
    def __init__(self,max_size = None):
        self.head = None
        self.tail = None
        self.max_size = max_size
        self.size = 0

    def peek(self):
        if self.is_empty() == True:
            print("Nothing to see here!")
        else:
            return self.head.get_value()
    
    def get_size(self):
        return self.size
    
    def has_space(self):
        if self.max_size == None:
            return True
        elif self.max_size > self.get_size():
            return True
        else:
            return False
        
    def is_empty(self):
        if self.get_size() == 0:
            return True
        else:
            return False
        
    def enqueue(self, value):
        if self.has_space() == True:
            item_to_add = Node(value)
            print("Adding " + str(item_to_add.get_value()) + " to the queue!")
            if self.is_empty() == True:
                dll.add_to_head(item_to_add)
                dll.add_to_tail(item_to_add)
            else:
                dll.add_to_tail(item_to_add)
            self.size += 1
        else:
            print("Sorry, no more room!")
        
q = Queue()
q.enqueue("all the fluffy kitties")
        
