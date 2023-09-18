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

## Hash Tables

```python
#phone_book = dict()
#or
# python dictionary == hash tabels
# key and value pair

phone_book = {}

phone_book["jenny"] = 898343
phone_book["emergency"] = 911

print(phone_book["jenny"])
print(phone_book["emergency"])


voted = {}

def check_voter(name):
    if voted.get(name):
        print("kick them out")
    else:
        voted[name] = True
        print("Let them vote")


check_voter("mike")
check_voter("tom")
check_voter("tom")


# Simple cache 

cache = {}

def get_page(url):
    if cache.get(url):
        return cache[url]
    else:
        data = get_data_from_server(url)
        cache[url] = data
        return data


# hashes good ofr caching 

''' 
You'll almost never have to implement a hash table yourself.
modeling relationships from one thing to another thing
filtering out duplicates
caching/memorizing data instead of making your server do work
hashes tables have really fast search, insert, and delete
once your load factor is greater thatn .07, its times to resize your hash table.
hash tables are great for catching duplicates
Average case of hash - O(1)  constant time

      hash tables hash tables Arrays Linked Lists 
       (avarage)    (worst)
search O(1)         O(n)        O(1)     O(n)
insert O(1)         O(n)        O(n)     O(1) 
delete O(1)         O(n)        O(n)     O(1)
'''

```

## Breadth-First Search

Graphs are a way to model how different things are connected to one another. It consists of several nodes.
To find the shortest path, there are two questions that breadth-first search can answer for you:
> Quection type 1 - Is there a path from node A to node B ? 
> Quection type 2 - What is the shortest path from node A to node B ? 

Queues - there are two operations in queues, enqueue and dequeue
ENQUEUE - Add an item to the queue == PUSH
DEQUEUE - Take and item off the queue == POP

The queue is called a FIFO data structure: First In, First Out
The Stack is a LIFO data structure:  Last In, First Out

```python
from collections import deque

# Define the graph with relationships
graph = {
    "you": ["alice", "bob", "claire"],
    "bob": ["anuj", "peggy"],
    "claire": ["thom", "jonny"],
    "anuj": [],
    "peggy": [],
    "thom": [],
    "jonny": []
}

def search(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = []
    while search_queue:
        person = search_queue.popleft()
        if person not in searched and person in graph:
            if person_is_seller(person):
                print(person + " is a mango seller!")
                return True
            else:
                search_queue += graph[person]
                searched.append(person)
    return False

def person_is_seller(name):
    return name[-1] == 'm'  # Check if the name ends with 'mango'

search("you")
'''
Breadth-first search takes O(number of people + number of edges), and it's more commonly written as O(V+E) V for number of vertices, E for number of edges.
Breadth-first search tells you if there's a path from A to B.
If there's path, breadth-first search-first will find the shortest path.
If you have a problem like "find the shortest X", try modeling your problem as a graph, and use breadth-first  search to solve.
A directed graph has arrows, and the relationship follows the direction of the arrow (rama -> adit means "rama owes adit  money").
undirected graphs don't have arrows, and the relationship goes both ways, (ross - rachel means "ross dated rachel and rachel dated ross").
You need to check people in the order they were added to the search list, so the search list needs to be a queue. Otherwise, you won't get the shortest path.
Once you check someone, make sure you don't check them again.  Otherwise, you might end up in an infinite loop.
'''
```

## Dijkstra's Algorithm

Steps :
1. Find the cheapest node. This is the node you can get to in the least amount of time.
2. Check whether there's a cheaper path to the neighbors of this node. If so, update their costs.
3. Repeat until you've done this for every node in the graph.
4. Calculate the final path.

When you work with Dijkdtra's algorithm, each edge in the graph has a number associated with it. These are called weights.

A graph with weights is called a weighted graph. A graph without weights is called an unweighted graph.

To calculate the shortest path in an unweighted graph, use breadth-first search.
To calculate the shortest path in a weighted graph, use Dijkstra's algorithm.
Graphs can also have cycles.

An undirected graph means that both nodes point to each other. That's a cycle! 
With an undirected graph, each edge adds another cycle. Dijkstra's algorithm only works with directed acyclic graphs, called DAGs for short.

```python
graph = {}

graph["you"] = ["alice", "bob", "claire"]
graph["start"] = {}
graph["start"]["a"] = 6
graph["start"]["b"] = 2
graph["a"] = {}
graph["a"]["fin"] = 1
graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["fin"] = 5
graph["fin"] = {}

infinity = float("inf")
costs = {}
costs["a"] = 6 
costs["b"] = 2
costs["fin"] = infinity

parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["fin"] = None

processed = []

node = find_lowest_cost_node(costs)
while node in not None:
    cost = costs[node]
    neighbors = graph[node]
    for n in neighbors.keys():
        new_cost = cost + neighbors[n]
        if costs[n] > new_cost:
            costs[n] = new_cost
            parents[n] = find_lowest_cost_node
    processed.append(node)
    node = find_lowest_cost_node(costs)

def find_lowest_cost_node(costs):
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in costs:
        cost = costs[nodes]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return find_lowest_cost_node

'''
> Breadth-first search is used  to calculate the shortest path for an unweighted graph
> Dijkstra's algorithm is used to calculate the shortest path for a weighted graph.
> Dijkstra's algorithm works when all the weights are positive.
> If you have negative weights, use the Bellman-Ford algorithm.
'''

```
### Credits goes to Aditya Y. Bhargava - grokking algorithms Book

