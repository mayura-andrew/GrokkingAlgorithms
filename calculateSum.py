# Recursive function
def sum(arr):
    if len(arr) == 0:
        return 0
    else:
        return arr[0] + sum(arr[1:])


def sum(arr):
    total_sum = 0  # Initialize the sum variable
    for i in range(len(arr)):  # Use range() to iterate through the indices of the list
        total_sum += arr[i]  # Add the current element to the sum
    return total_sum  # Return the final sum

# Test with an empty list, should return 0
# print(sum([]))  # Output: 0

# # Test with a list of single element, should return the element itself
# print(sum([5]))  # Output: 5

# # Test with a list of positive integers
# print(sum([1, 2, 3, 4, 5]))  # Output: 15 (1 + 2 + 3 + 4 + 5 = 15)

# # Test with a list of negative integers
# print(sum([-1, -2, -3, -4, -5]))  # Output: -15 (-1 + (-2) + (-3) + (-4) + (-5) = -15)

# # Test with a list containing both positive and negative integers
# print(sum([1, -2, 3, -4, 5]))  # Output: 3 (1 + (-2) + 3 + (-4) + 5 = 3)

def max_index(arr):
    max_val = arr[0]
    max_index = 0
    for i in range(len(arr)):
        if arr[i] > max_val:
            max_val = arr[i]
            max_index = i
    print(arr[max_index])
    return max_index

max_index([1, 2, 3, 4, 5])  # Output: 15 (1 + 2 + 3 + 4 + 5 = 15)

def max(list):
	if len(list) == 2:
		return list[0] if list[0] > list[1] else list[1]
	sub_max = max(list[1:])
	return list[0] if list[0] > sub_max else sub_max


def max_value(lst):
    if not lst:  # Base case: if the list is empty, return None or raise an exception
        return None  # You can return None or raise an exception, depending on your preference.
    elif len(lst) == 1:
        return lst[0]
    elif len(lst) == 2:
        return lst[0] if lst[0] > lst[1] else lst[1]
    
    mid = len(lst) // 2
    left_max = max_value(lst[:mid])
    right_max = max_value(lst[mid:])
    
    return left_max if left_max > right_max else right_max



def count(list):
	if list == []:
		return 0
	return 1 + count(list[1:])


# Test with an empty list, should return None
print(max_value([]))  # Output: None

# Test with a list of a single element, should return the element itself
print(max_value([5]))  # Output: 5

# Test with a list of positive integers
print(max([1, 2, 3, 4, 5]))  # Output: 5 (maximum value is 5)

# Test with a list of negative integers
print(max_value([-1, -2, -3, -4, -5]))  # Output: -1 (maximum value is -1)

# Test with a list containing both positive and negative integers
print(max_value([1, -2, 3, -4, 5]))  # Output: 5 (maximum value is 5)

# Test with a list containing duplicate maximum values
print(max_value([5, 5, 5, 5, 5]))  # Output: 5 (maximum value is 5)

# Test with a large list
print(max_value([9, 8, 7, 6, 10, 12, 15, 13, 11]))  # Output: 15 (maximum value is 15)
