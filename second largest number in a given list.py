def find_second_largest(numbers):
    unique_numbers = list(set(numbers))
    unique_numbers.sort()
    return unique_numbers[-2]
numbers_list = [10, 20, 4, 45, 99]
second_largest = find_second_largest(numbers_list)
print("The second largest number in the list is:", second_largest)
