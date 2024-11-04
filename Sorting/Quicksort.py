from random import randrange, shuffle

def quicksort(list, start, end):
    if start >= end:
        return
    
    pivot_idx = randrange(start, end + 1)
    pivot_element = list[pivot_idx]
    
    list[end], list[pivot_idx] = list[pivot_idx], list[end]

    less_than_pointer = start

    for idx in range(start, end):
        if list[idx] < pivot_element:
            list[less_than_pointer], list[idx] = list[idx], list[less_than_pointer]
            less_than_pointer += 1
    list[end], list[less_than_pointer] = list[less_than_pointer], list[end]
    

    quicksort(list, start, less_than_pointer - 1)
    quicksort(list, less_than_pointer + 1, end)

unsorted_list = [3,7,12,24,36,42]
shuffle(unsorted_list)
print(unsorted_list)

quicksort(unsorted_list, 0, len(unsorted_list) - 1)
print(unsorted_list)