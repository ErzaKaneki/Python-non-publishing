# def sum_to_one(n):
#     result = 1
#     call_stack = []

#     while n != 1:
#         execution_context = {"n_value": n}
#         call_stack.append(execution_context)
#         n -= 1
#         print(call_stack)
#     print("BASE CASE REACHED")
#     while call_stack:
#         return_value = call_stack.pop()
#         print("\nAdding return_value {0} to result {1}".format(return_value["n_value"], result))
#         result += return_value["n_value"]
#         print(call_stack)
#     return result, call_stack

# sum_to_one(4)


# def sum_to_one(n):
#     if n == 1:
#         print("Recursing with input: {0}".format(n))
#         return n
#     elif n != 1:
#         print("Recursing with input: {0}".format(n))
#         return n + sum_to_one(n - 1)
    
# print(sum_to_one(7))


# def factorial(n):
#     if n == 1:
#         return n
#     elif n != 1:
#         return n * factorial(n - 1)
    
# print(factorial(12)) #found that this only works up to 998 XD  999 and up will throw a RecursionError

#POWER SETS @.@
# def power_set(my_list):
#     # base case: an empty list
#     if len(my_list) == 0:
#         return [[]]
#     # recursive step: subsets without first element
#     power_set_without_first = power_set(my_list[1:])
#     # subsets with first element
#     with_first = [ [my_list[0]] + rest for rest in power_set_without_first ]
#     # return combination of the two
#     return with_first + power_set_without_first
  
# universities = ['MSU', 'UND', 'NDSU', 'NDSCS']
# power_set_of_universities = power_set(universities)

# for set in power_set_of_universities:
#   print(set)

#UNPACKING LISTS WITH RECURSION
# def flatten(my_list):
#     result = []
#     for item in my_list:
#         if isinstance(item, list):
#             #print("List found!")
#             flat_list = flatten(item)
#             for element in  item:
#                 if isinstance(element, list):
#                     flat_element = flatten(element)
#                     for spec in element:
#                         result.append(spec)
#                 else:        
#                     result.append(element)
#         else:
#             result.append(item)
#     return result

# planets = ['mercury', 'venus', ['earth'], 'mars', [['jupiter', 'saturn']], 'uranus', ['neptune', 'pluto']]

# print(flatten(planets))


# def fibonacci(n):
#     if n == 1:
#         return 1
#     if n == 0:
#         return 0
#     return fibonacci(n - 1) + fibonacci(n - 2)

# print(fibonacci(5))
# print(fibonacci(10))
# print(fibonacci(7))

# fibonacci_runtime = "2^N"


# def build_bst(my_list):
#     if len(my_list) == 0:
#         return "No Child"
#     middle_idx = len(my_list) // 2
#     middle_value = my_list[middle_idx]
#     print("Middle index: {I}".format(I = middle_idx))
#     print("Middle value: {V}".format(V = middle_value))
#     tree_node = {"data":middle_value}
#     tree_node["left_child"] = build_bst(my_list[:middle_idx])
#     tree_node["right_child"] = build_bst(my_list[middle_idx + 1:])
#     return tree_node

# sorted_list = [12, 13, 14, 15, 16]
# binary_search_tree = build_bst(sorted_list)
# print(binary_search_tree)

# runtime = "N*logN"


# def factorial(n):
#     if n < 0:
#         return ValueError("Inputs 0 or larger only")
#     if n <= 1:
#         return 1
#     while n > 1:
#         product = n * (n - 1)
#         n -= 1
#         return product


# print(factorial(3) == 6) #True
# print(factorial(0) == 1) #True
# print(factorial(5) == 120) #False


# def fibonacci(n):
#     fibs = [0, 1]

#     if n <= len(fibs) - 1:
#         return n
#     else:
#         while n > len(fibs) - 1:
#             next_fib = fibs[(len(fibs) - 1)] + fibs[(len(fibs) - 2)]
#             fibs.append(next_fib)

#         return fibs[n]


# print(fibonacci(3) == 2)
# print(fibonacci(7) == 13)
# print(fibonacci(0) == 0)


# def sum_digits(n):
#     if n <= 9:
#         return n
#     last_digit = n % 10
#     return sum_digits(n // 10) + last_digit

# print(sum_digits(12) == 3)
# print(sum_digits(552) == 12)
# print(sum_digits(123456789) == 45)


# def find_min(my_list, min = None):
#     if not my_list:
#         return min
#     else:
#         if not min or my_list[0] < min:
#             min = my_list[0]
#         return find_min(my_list[1:], min)
        
    

# print(find_min([42, 17, 2, -1, 67]) == -1)
# print(find_min([]) == None)
# print(find_min([13, 72, 19, 5, 86]) == 5)


# def is_palindrome(my_string):
#     if len(my_string) < 2:
#         return True
#     if my_string[0] != my_string[-1]:
#         return False
#     return is_palindrome(my_string[1:-1])



# print(is_palindrome("abba") == True)
# print(is_palindrome("abcba") == True)
# print(is_palindrome("") == True)
# print(is_palindrome("abcd") == False)


# def multiplication(num_1, num_2):
#     if num_1 == 0 or num_2 == 0:
#         return 0
#     if num_2 > 0:
#         return num_1 + multiplication(num_1, num_2 - 1)
        
# print(multiplication(3, 7) == 21)
# print(multiplication(5, 5) == 25)
# print(multiplication(0, 4) == 0)


# def depth(tree):
#     if tree == None:
#         return 0
    
#     left_depth = depth(tree["left_child"])
#     right_depth = depth(tree["right_child"])

#     if left_depth > right_depth:
#        return left_depth + 1
#     else:
#        return right_depth + 1

# def build_bst(my_list):
#   if len(my_list) == 0:
#     return None

#   mid_idx = len(my_list) // 2
#   mid_val = my_list[mid_idx]

#   tree_node = {"data": mid_val}
#   tree_node["left_child"] = build_bst(my_list[ : mid_idx])
#   tree_node["right_child"] = build_bst(my_list[mid_idx + 1 : ])

#   return tree_node

# # HELPER VARIABLES
# tree_level_1 = build_bst([1])
# tree_level_2 = build_bst([1, 2, 3])
# tree_level_4 = build_bst([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]) 

# # test cases
# print(depth(tree_level_1) == 1)
# print(depth(tree_level_2) == 2)
# print(depth(tree_level_4) == 4)


# def move_to_end(lst, val):
#     result = []
#     if len(lst) == 0:
#         return []
    
#     if lst[0] == val:
#         result += move_to_end(lst[1:], val)
#         result.append(lst[0])
#     else:
#         result.append(lst[0])
#         result += move_to_end(lst[1:], val)
#     return result

# gemstones = ["Amber", "Sapphire", "Amber", "Jade"]
# print(move_to_end(gemstones, "Amber"))


def wrap_string(str, n):
    result = ""
    if n <= 0:
        return str
    result = "<" + wrap_string(str, n - 1) + ">"
    return result

wrapped = wrap_string("Pearl", 3)
print(wrapped)