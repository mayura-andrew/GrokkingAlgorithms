def findSmallest(arr):
    smallest = arr[0]  # stores the smallest vlaue
    smallest_index = 0  # stores the index of the smallest value
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    print(smallest)
    return smallest_index

def selectionSort(arr):
    newArr = []
    for i in range(len(arr)):
        smallest = findSmallest(arr)
        print(smallest)
        newArr.append(arr.pop(smallest))
        print(arr)
        print(newArr)
    print(newArr)
    print(arr)
    return newArr

print(selectionSort([5, 3, 6, 3, 10]))

## Time complexity of this selection sort alogorithm is O(n2)
