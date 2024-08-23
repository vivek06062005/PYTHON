def find_max_min_elements(input_list):
    max_element = max(input_list)
    min_element = min(input_list)
    return max_element, min_element
my_list = [10, 5, 20, 8, 15]
max_num, min_num = find_max_min_elements(my_list)
print(f"Maximum element: {max_num}")
print(f"Minimum element: {min_num}")
