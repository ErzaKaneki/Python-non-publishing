class MaxHeap:
    def __init__(self):
        self.heap_list = [None]
        self.count = 0

    def parent_idx(self, idx):
        return idx // 2
        
    def left_child_idx(self, idx):
        return idx * 2
        
    def right_child_idx(self, idx):
        return idx * 2 + 1
    
    def child_present(self, idx):
        return self.left_child_idx(idx) <= self.count
        
    def add(self, element):
        self.count += 1
        print("adding: {0} to {1}".format(element, self.heap_list))
        self.heap_list.append(element)
        self.heapify_up()

    def heapify_up(self):
        print("Heapifying up")
        idx = self.count
        while self.parent_idx(idx) > 0:
            child = self.heap_list[idx]
            parent = self.heap_list[self.parent_idx(idx)]
            if parent < child:
                print("Swapping {0} with {1}".format(parent, child))
                self.heap_list[idx] = parent
                self.heap_list[self.parent_idx(idx)] = child
            idx = self.parent_idx(idx)
        print("Heap Restored {0}".format(self.heap_list))

    def retrieve_max(self):
        if self.count == 0:
            print("No items in heap")
            return None
        max_val = self.heap_list[1]
        print("Removing: {0} from {1}".format(max_val, self.heap_list))
        self.heap_list[1] = self.heap_list[self.count]
        self.count -= 1
        self.heap_list.pop()
        print("Last element moved to first: {0}".format(self.heap_list))
        self.heapify_down()
        return max_val
    
    def heapify_down(self):
        idx = 1
        while self.child_present(idx):
            print("Heapifying down!")
            larger_child_idx = self.get_larger_child_idx(idx)
            child = self.heap_list[larger_child_idx]
            parent = self.heap_list[idx]
            if parent < child:
                self.heap_list[idx] = child
                self.heap_list[larger_child_idx] = parent
            idx = larger_child_idx
        print("Heap Restored!\n{0}".format(self.heap_list))
            

    def get_larger_child_idx(self, idx):
        if self.right_child_idx(idx) > self.count:
            print("There is only a left child")
            return self.left_child_idx(idx)
        else:
            left_child = self.heap_list[self.left_child_idx(idx)]
            right_child = self.heap_list[self.right_child_idx(idx)]
            if left_child > right_child:
                print("Left child is larger than Right child")
                return self.left_child_idx(idx)
            else:
                print("Right child is larger than Left child")
                return self.right_child_idx(idx)
