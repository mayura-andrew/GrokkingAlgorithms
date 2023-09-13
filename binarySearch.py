def binary_search(list, item):
    low = 0
    high = len(list) - 1
    
    while low <= high:
        mid = (low + high) // 2
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
            
        else:
            low = mid + 1
    return None



my_list = [1, 3, 5, 6, 7, 9]

print(binary_search(my_list, 7));

# Binary search  - logarithmic time O(log n)

# Simple search - linear time O(n) 

# Big O notation - O(n) - worst case scenario

# Big O notation is special that tells you know fast an algorithm is. 
# It is a way of measuring how long an algorithm takes to run. 
# It is a way of comparing the number of operations an algorithm will take to complete based on the input size.
# Binary search only works if that list sorted (sorted items only)
