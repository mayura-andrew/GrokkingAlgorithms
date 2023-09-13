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

