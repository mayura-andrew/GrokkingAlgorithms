# Grokking Algorithms

This README provides code examples and explanations for the algorithms covered in the book "Grokking Algorithms" by Aditya Y. Bhargava. These algorithms are essential for understanding and solving various computer science and programming problems.

## Table of Contents

- [Binary Search](#binary-search)
- [Selection Sort](#selection-sort)
- [Recursion](#recursion)
- [Quicksort](#quicksort)
- [Hash Tables](#hash-tables)
- [Breadth-First Search](#breadth-first-search)
- [Dijkstra's Algorithm](#dijkstras-algorithm)
- [Greedy Algorithms](#greedy-algorithms)
- [Dynamic Programming](#dynamic-programming)

## Binary Search

Binary search is a fundamental algorithm for efficiently searching for an element in a sorted array. It divides the search space in half with each step.


```python
# Python code example for binary search
def binary_search(list, target):
    low = 0 
    high = len(list) - 1
    while (low <= high):
        mid = (low + high) // 2
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None

    ## Time Complexity: O(log n) - Logarithmic


```

## Simple (Linear) Search 

```python
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Target element found at index i
    return -1  # Target element not found

# Example usage
arr = [2, 4, 6, 8, 10, 12, 14]
target = 10
result = linear_search(arr, target)
if result != -1:
    print(f"Element {target} found at index {result}")
else:
    print(f"Element {target} not found in the array")


    # Time Complexity: O(n) - Linear 


```

## Selection Sort

Selection sort is a neat algorithm, but it's not very fast. Quicksort is a faster sorting algorithm that only takes O(n log n) time. 

```python

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
        newArr.append(arr.pop(smallest))
    return newArr

print selectionSort([5, 3, 6, 3, 10])

# Time Complexity: O(n2) 