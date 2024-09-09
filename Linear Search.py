def linear_search(search_list, target_value):
    for i in range(len(search_list)):
        print(search_list[i])
        if search_list[i] == target_value:
            return i
    raise ValueError("{0} not in list".format(target_value))

values = [54, 22, 46, 99]
print(linear_search(values, 22))