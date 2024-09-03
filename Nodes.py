#NODES    XD
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
# class Node:
#     def __init__(self, value, next_node = None):
#         self.value = value
#         self.next_node = next_node

#     def get_value(self):
#         return self.value
    
#     def get_next_node(self):
#         return self.next_node

#     def set_next_node(self, next_node):
#         self.next_node = next_node
#         return self.next_node
    

# class LinkedList:

#     def __init__(self, value = None):
#         self.head_node = Node(value)

#     def get_head_node(self):
#         return self.head_node
    
#     def insert_beginning(self, new_value):
#         new_node = Node(new_value)
#         new_node.set_next_node(self.head_node)
#         self.head_node = new_node
    
#     def stringify_list(self):
#         end_string = ""
#         current_node = self.get_head_node()
#         while current_node:
#             if current_node.get_value() != None:
#                 end_string += str(current_node.get_value()) + "\n"
#             current_node = current_node.get_next_node()
#         return end_string

#     def remove_node(self, value_to_remove):
#         current_node = self.head_node
#         if current_node.get_value() == value_to_remove:
#             self.head_node = self.head_node.get_next_node()
#             current_node = self.head_node
#         else:
#             while current_node:
#                 previous_node = current_node
#                 current_node = current_node.next_node
#                 if current_node.get_value() == value_to_remove:
#                     previous_node.next_node = current_node.next_node  #OR-> current_node.set_next_node(next_node.get_next_node()) <- TRANSPARENCY
#                     current_node = None

# LL = LinkedList()
# LL.insert_beginning(5)
# LL.insert_beginning(52)
# LL.insert_beginning(3)
# LL.insert_beginning(9)
# LL.insert_beginning(3)
# LL.insert_beginning(7)
# LL.remove_node(3)        
# print(LL.stringify_list())


#SWAPPING TWO NODES PREV_NODE1 & NODE1 SEARCH FOR FIRST NODE
#                   PREV_NODE2 & NODE2 SEARCH FOR OTHER NODE
#                   IF EITHER NODE PREV_NODE = NONE MEANS HEAD SO MAKE THE SWAP TO THE HEAD
#                   OTHERWISE PREV_NODE1.NEXT_NODE = NODE2
#                         AND NODE1.NEXT_NODE = NODE2.NEXT_NODE
#                   ALSO PREV_NODE2.NEXT_NODE = NODE1
#                         AND NODE2.NEXT_NODE = NODE1.NEXT_NODE
#  REMEMBER ->      IF NODE1 IS NONE OR NODE2 IS NONE  CAN'T SWAP
#                   IF VAL1 == VAL2: -> PRINT WARNING -> RETURN  DON'T SWAP SAME VAL'S POINTLESS RUN TIME


#SWAPPING NODE EXAMPLE  SWAPS 9 WITH 5
# def swap_nodes(input_list, val1, val2):
#   print(f'Swapping {val1} with {val2}')

#   node1_prev = None
#   node2_prev = None
#   node1 = input_list.head_node
#   node2 = input_list.head_node

#   if val1 == val2:
#     print("Elements are the same - no swap needed")
#     return

#   while node1 is not None:
#     if node1.get_value() == val1:
#       break
#     node1_prev = node1
#     node1 = node1.get_next_node()

#   while node2 is not None:
#     if node2.get_value() == val2:
#       break
#     node2_prev = node2
#     node2 = node2.get_next_node()

#   if (node1 is None or node2 is None):
#     print("Swap not possible - one or more element is not in the list")
#     return

#   if node1_prev is None:
#     input_list.head_node = node2
#   else:
#     node1_prev.set_next_node(node2)

#   if node2_prev is None:
#     input_list.head_node = node1
#   else:
#     node2_prev.set_next_node(node1)

#   temp = node1.get_next_node()
#   node1.set_next_node(node2.get_next_node())
#   node2.set_next_node(temp)


# ll = LinkedList.LinkedList()
# for i in range(10):
#   ll.insert_beginning(i)

# print(ll.stringify_list())
# swap_nodes(ll, 9, 5)
# print(ll.stringify_list())


#FINDING nTH NODE WITH 2 RUNNERS
# def nth_last_node(linked_list, n):
#   claimer = None
#   explorer = linked_list.head_node
#   count = 1
#   while explorer:
#     explorer = explorer.get_next_node()
#     count += 1
#     if count >= n + 1:
#       if claimer is None:
#         claimer = linked_list.head_node
#       else:
#         claimer = claimer.get_next_node()
#   return claimer

# def generate_test_linked_list():
#   linked_list = LinkedList()
#   for i in range(50, 0, -1):
#     linked_list.insert_beginning(i)
#   return linked_list

# test_list = generate_test_linked_list()
# print(test_list.stringify_list())
# nth_last = nth_last_node(test_list, 4)
# print(nth_last.value)


#USING TWO RUNNERS TO FIND MIDDLE OF THE LINKEDLIST (FAST AND SLOW)
# def find_middle(linked_list):
#   claimer = linked_list.head_node
#   explorer = linked_list.head_node
#   while explorer:
#     explorer = explorer.get_next_node()
#     if explorer:
#       explorer = explorer.get_next_node()
#       claimer = claimer.get_next_node()
#   return claimer

# def generate_test_linked_list(length):
#   linked_list = LinkedList()
#   for i in range(length, 0, -1):
#     linked_list.insert_beginning(i)
#   return linked_list

# test_list = generate_test_linked_list(7)
# print(test_list.stringify_list())
# middle_node = find_middle(test_list)
# print(middle_node.value)

#CAN ALSO USE A MODULO EXPRESSION TO MOVE SLOWER RUNNER
# def find_middle_alt(linked_list):
#   count = 0
#   explorer = linked_list.head_node
#   claimer = linked_list.head_node
#   while explorer:
#     explorer = explorer.get_next_node()
#     if count % 2 != 0:
#       claimer = claimer.get_next_node()
#     count += 1
#   return claimer


#NODE CLASS AND CONSTRUCTOR DOUBLY LINKED LIST
class Node:
  def __init__(self, value, next_node=None, prev_node=None):
    self.value = value
    self.next_node = next_node
    self.prev_node = prev_node
    
  def set_next_node(self, next_node):
    self.next_node = next_node
    
  def get_next_node(self):
    return self.next_node

  def set_prev_node(self, prev_node):
    self.prev_node = prev_node
    
  def get_prev_node(self):
    return self.prev_node
  
  def get_value(self):
    return self.value
    

class DoublyLinkedList:
  def __init__(self, head_node = None, tail_node = None):
    self.head_node = head_node
    self.tail_node = tail_node

  def add_to_head(self, new_value):
    new_head = Node(new_value)
    current_head = self.head_node
    
    if current_head != None:
      current_head.set_prev_node(new_head)
      new_head.set_next_node(current_head)

    self.head_node = new_head

    if self.tail_node == None:
      self.tail_node = new_head

  def add_to_tail(self, new_value):
    new_tail = Node(new_value)
    current_tail = self.tail_node

    if current_tail != None:
      current_tail.set_prev_node(new_tail)
      new_tail.set_next_node(current_tail)
    
    self.tail_node = new_tail

    if self.head_node == None:
      self.head_node = new_tail

#REMOVING THE HEAD (DOUBLY)

  def remove_head(self):
    
    removed_head = self.head_node
    
    if removed_head.value == None:
      return None
    
    self.head_node = removed_head.get_next_node()
    
    if self.head_node != None:
      self.head_node.prev_node = None

    if removed_head == self.tail_node:
      self.remove_tail()

    return removed_head.get_value()
  
#REMOVING THE TAIL

  def remove_tail(self):
    
    removed_tail = self.tail_node
    
    if removed_tail.value == None:
      return None
    
    self.tail_node = removed_tail.get_prev_node()
    
    if self.tail_node != None:
      self.tail_node.next_node = None

    if removed_tail == self.head_node:
      self.remove_head()

    return removed_tail.get_value()
  
#REMOVING BY VALUE I

  def remove_by_value(self, value_to_remove):

    node_to_remove = None

    current_node = self.head_node

    while current_node != None:
      if current_node.get_value() == value_to_remove:
        node_to_remove = current_node
        break

      current_node = current_node.get_next_node()

    if node_to_remove == None:
      return None  
    
#REMOVING BY VALUE II

    if node_to_remove == self.head_node:
      self.remove_head()
    elif node_to_remove == self.tail_node:
      self.remove_tail()
    else:
      next_node = node_to_remove.get_next_node()
      prev_node = node_to_remove.get_prev_node()
      next_node.set_prev_node(prev_node)
      prev_node.set_next_node(next_node)
    
    return node_to_remove
  
#USING THE LIST

  def stringify_list(self):
    
    string_list = ""
    current_node = self.head_node
    
    while current_node:
      
      if current_node.get_value() != None:
        string_list += str(current_node.get_value()) + "\n"
      
      current_node = current_node.get_next_node()
    
    return string_list
  
subway = DoublyLinkedList()  
subway.add_to_head("Times Square")
subway.add_to_head("Grand Central")
subway.add_to_head("Central Park")

print(subway.stringify_list())