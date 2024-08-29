# class Node:
#     def __init__(self, value, link_node = None):
#         self.value = value
#         self.link_node = link_node

#     def get_value(self):
#         return self.value

#     def get_link_node(self):
#         return self.link_node
    
#     def set_link_node(self, link_node):
#         self.link_node = link_node
#         return self.link_node

# yacko = Node("likes to yak")
# wacko = Node("has a penchant for hoarding snacks")
# dot = Node("enjoys spending time in movie lots")

# yacko.set_link_node(dot) #YACKO IS LINKED TO DOT
# dot.set_link_node(wacko) #DOT IS LINKED TO WACKO
# #COULD USE THIS IN A DIRECTORY OR A HEIRACHEY FLOW
# dots_data = yacko.get_link_node().get_value()  #YACKO GET LINK = DOT SO THE GETTER IS RETREIVING DOTS VALUE
# wackos_data = dot.get_link_node().get_value()  #DOT GET LINK = WACKO SO THE GETTER IS RETRIEVING WACKOS VALUE

# print(dots_data)
# print(wackos_data)


#NODE IMPLEMENTATION
class Node:
    def __init__(self, value, next_node = None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value
    def get_next_node(self):
        return self.next_node

    def set_next_node(self, next_node):
        self.next_node = next_node
        return self.next_node
    
my_node = Node(44)

class LinkedList:

    def __init__(self, value = None):
        self.head_node = Node(value)

    def get_head_node(self):
        return self.head_node
    
    def insert_beginning(self, new_value):
        new_node = Node(new_value)
        new_node.set_next_node(self.head_node)
        self.head_node = new_node
    
    def stringify_list(self):
        end_string = ""
        current_node = self.get_head_node()
        while current_node:
            if current_node.get_value() != None:
                end_string += str(current_node.get_value()) + "\n"
            current_node = current_node.get_next_node()
        return end_string

        
ll = LinkedList(5)
ll.insert_beginning(70)
ll.insert_beginning(5675)
ll.insert_beginning(90)
print(ll.stringify_list())