def findSmallest(arr):
    smallest = arr[0]  # stores the smallest vlaue
    smallest_index = 0  # stores the index of the smallest value
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

print(findSmallest([4,5,7,8,22]))
