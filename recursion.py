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


def power_set(my_list):
    # base case: an empty list
    if len(my_list) == 0:
        return [[]]
    # recursive step: subsets without first element
    power_set_without_first = power_set(my_list[1:])
    # subsets with first element
    with_first = [ [my_list[0]] + rest for rest in power_set_without_first ]
    # return combination of the two
    return with_first + power_set_without_first
  
universities = ['MSU', 'UND', 'NDSU', 'NDSCS']
power_set_of_universities = power_set(universities)

for set in power_set_of_universities:
  print(set)
