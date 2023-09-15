# Grokking Algorithms

This README provides code examples and explanations for the algorithms covered in the book "Grokking Algorithms" by Aditya Y. Bhargava. These algorithms are essential for understanding and solving various computer science and programming problems.

## Table of Contents

- [Binary Search](#binary-search)
- [Simple (Linear) Search](#simple-search)
- [Selection Sort](#selection-sort)
- [Recursion](#recursion)
- [Quicksort](#quicksort)
- [Hash Tables](#hash-tables)
- [Breadth-First Search](#breadth-first-search)
- [Dijkstra's Algorithm](#dijkstras-algorithm)
- [Greedy Algorithms](#greedy-algorithms)
- [Dynamic Programming](#dynamic-programming)

## Binary Search

Binary search is a fundamental algorithm for efficiently searching for an element in a sorted array. 
It divides the search space in half with each step. 
Binary search is a lot faster than simple search. 
O(log n) is faster than O(n), but it gets a lot faster once the list of items you're searching through grows. 
Algorithm  speed isn't measured in seconds. 
Algorithm times are measured in terms of growth of an algorithm. 
Algorithm times are written in Big O notation.


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

## Simple Search 

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

Arrays allows fast reads. - O(1)  
List [Read] - O(n)
Linked lists allow fast inserts and deletes - O(1) 
Arrays[Insert && Delete] - O(n)

All elements in the array should be the same type (all ints, all doubles, and so on). 

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

# Time Complexity: O(n2) 
```

## Recursion 

Recursion is when a function calls itself. 
Every recursive function has two case: the base case amd the recursive case. 
A stack has two operations: push and pop; 
The stack plays a big part in recursion. 
All functions calls go onto the call stack. 
The call stack can get very large, which takes up a lot of memory.

```python

def factorial(n):
    if (n == 1):
        return 1 # Base Case
    else:
        return n * factorial(n-1)   # recursion 
        
    # Time Complexity: O(n) - Linear 

```

.....

## Quick Sort 
Divide and Conquer (D&C) works by breaking a problem down into smaller and smaller pieces. If you're using D&C on a list, the base case is probably an empty array or an array with on element.
If you're implementing quicksort, choose a random element as the pivot. The average runtime of quicksort is O(n log n)!
The constant in Big O notation can matter sometimes. That's why quicksort faster than merge sort.
The constant almost never matters for simple search versus binary search, because O(log n) is so much faster than 0(n) when your list gets big.

```python
def quickSort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot] # sub-array of all the elements less than the pivot
        greater = [i for i in array[1:] if i > pivot] # sub-array of all the elements greater than the pivot
        return quickSort(less) + [pivot] + quickSort(greater)

# Time complexity - O(n log n)
# worst case - O(n^2)
# average case - O(n log n) 
# Quick Sort is unique because its speed depends on the pivot you choose.
```
### Credits goes to Aditya Y. Bhargava - grokking algorithms Book

