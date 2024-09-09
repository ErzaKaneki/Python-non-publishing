# def linear_search(search_list, target_value):
#     for i in range(len(search_list)):
#         print(search_list[i])
#         if search_list[i] == target_value:
#             return i
#     raise ValueError("{0} not in list".format(target_value))

# values = [54, 22, 46, 99]
# print(linear_search(values, 22))


# number_list = [ 10, 14, 19, 26, 27, 31, 33, 35, 42, 44]
# target_number = 33

# def linear_search(search_list, target_value):
#   for idx in range(len(search_list)):
#     if search_list[idx] == target_value:
#       return idx
#   raise ValueError("{0} not in list".format(target_value))



# try:
#   # Call the function below...
#     print(linear_search(number_list, 100))
# except ValueError as error_message:
#   print("{0}".format(error_message))


# # Search list and target value
# tour_locations = [ "New York City", "Los Angeles", "Bangkok", "Istanbul", "London", "New York City", "Toronto"]
# target_city = "New York City"

# #Linear Search Algorithm
# def linear_search(search_list, target_value):
#     matches = []
#     for idx in range(len(search_list)):
#         if search_list[idx] == target_value:
#             matches.append(idx)
#     if matches != 0:
#         return matches
#     else:    
#         raise ValueError("{0} not in list".format(target_value))

# #Function call
# tour_stops = linear_search(tour_locations, target_city)
# print(tour_stops)
