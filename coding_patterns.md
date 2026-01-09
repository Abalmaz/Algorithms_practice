# Essential Coding Patterns 
This document outlines common algorithmic patterns, how they work, 
and provides a Python implementation for a standard use case of each.
### Table of Contents
- [Two Pointers](#1-two-pointers)
- [Fast & Slow Pointers](#2-fast--slow-pointers-tortoise-and-hare)
- [Sliding Window](#3-sliding-window)
- [Merge Intervals](#4merge-intervals)
- [Cyclic ](#5-cyclic-sort)
- [SortIn-place](#6-sort-in-place) 
- [Reversal of a Linked List](#6-in-place-reversal-of-a-linked-list)
- [Two Heaps](#7-two-heaps)
- [Modified Binary Search](#8-modified-binary-search)
- [Top 'K' Elements](#9-top-k-elements)
- [K-way Merge](#10-k-way-merge)
- [Topological Sort (Graph)](#11-topological-sort-graph)
- [SubsetsGreedy Techniques](#13-greedy-techniques)
- [Backtracking](#14-backtracking)
- [Dynamic Programming](#15-dynamic-programming)
- [Sort and Search](#16-sort-and-search)
- [Matrices](#17-matrices)
- [Stacks](#18-stacks)
- [Tree Depth First Search (DFS)](#19-tree-depth-first-search-dfs)
- [Trie (Prefix Tree)](#20-trie-prefix-tree)
- [Hash Maps](#21-hash-maps)
- [Knowing What to Track](#22-knowing-what-to-track)
- [Union Find (Disjoint Set)](#23-union-find-disjoint-set)

### 1. Two Pointers

**Concept:** The two pointers pattern is a versatile technique used in problem-solving to efficiently traverse or manipulate sequential data structures, such as arrays or linked lists. As the name suggests, it involves maintaining two pointers that traverse the data structure in a coordinated manner, typically starting from different positions or moving in opposite directions. These pointers dynamically adjust based on specific conditions or criteria, allowing for the efficient exploration of the data and enabling solutions with optimal time and space complexity. Whenever there’s a requirement to find two data elements in an array that satisfy a certain condition, the two pointers pattern should be the first strategy to come to mind.

The pointers can be used to iterate through the data structure in one or both directions, depending on the problem statement. For example, to identify whether a string is a palindrome, we can use one pointer to iterate the string from the beginning and the other to iterate it from the end. At each step, we can compare the values of the two pointers and see if they meet the palindrome properties. 

The naive approach to solving this problem would be using nested loops, with a time complexity of 
**O(n^2)**. However, by using two pointers moving toward the middle from either end, we exploit the symmetry property of palindromic strings. This allows us to compare the elements in a single loop, making the algorithm more efficient with a time complexity of 
**O(n)**.

**When to use:** 
 - Linear data structure: The input data can be traversed in a linear fashion, such as an array, linked list, or string.
 - Process pairs: Process data elements at two different positions simultaneously.
 - Dynamic pointer movement: Both pointers move independently of each other according to certain conditions or criteria. In addition, both pointers might move along the same or two different data structures.

**Examples for use:** 
 - Reversing an array: Given an array of integers, reverse it in place.
 - Pair with given sum in a sorted array: Given a sorted array of integers, find a pair in the array that sums to a number T.

**Use Case:** Finding a pair with a target sum in a sorted array.
```def pair_with_target_sum(arr, target_sum):
    left, right = 0, len(arr) - 1
    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == target_sum:
            return [left, right]  # Found the pair
        
        if target_sum > current_sum:
            left += 1  # We need a larger sum
        else:
            right -= 1 # We need a smaller sum
    return [-1, -1]

# Example
print(pair_with_target_sum([1, 2, 3, 4, 6], 6)) # Output: [1, 3] (indices of 2 and 4)
```
### 2. Fast & Slow Pointers (Tortoise and Hare)

**Concept:** Similar to the two pointers pattern, the fast and slow pointers pattern uses two pointers to traverse an iterable data structure, but at different speeds, often to identify cycles or find a specific target. The speeds of the pointers can be adjusted according to the problem statement. The two pointers pattern focuses on comparing data values, whereas the fast and slow pointers method is typically used to analyze the structure or properties of the data.

The key idea is that the pointers start at the same location and then start moving at different speeds. The slow pointer moves one step at a time, while the fast pointer moves by two steps. Due to the different speeds of the pointers, this pattern is also commonly known as the Hare and Tortoise algorithm, where the Hare is the fast pointer while Tortoise is the slow pointer. If a cycle exists, the two pointers will eventually meet during traversal. This approach enables the algorithm to detect specific properties within the data structure, such as cycles, midpoints, or intersections.

To visualize this, imagine two runners on a circular track starting at the same point. With different running speeds, the faster runner will eventually overtake the slower one, illustrating how this method works to detect cycles.

**When to use:** Linked Lists or Arrays involving cycles or finding a specific position (like the middle)
without knowing the length.
 - Linear data structure: The input data can be traversed in a linear fashion, such as an array, linked list, or string.
 - Cycle or intersection detection: The problem involves detecting a loop within a linked list or an array or involves finding an intersection between two linked lists or arrays.
 - Find the starting element of the second quantile: This means identifying the element where the second part of a divided dataset begins—like the second half, second third (tertile), or second quarter (quartile). For example, the task might ask you to find the middle element of an array or a linked list, which marks the start of the second half

**Examples for use:** 
 - Middle of the linked list: Given the head of a singly linked list, return the middle node of the linked list.
 - Detect cycle in an array: Given an array of non-negative integers where elements are indexes pointing to the next element, determine if there is a cycle in the array.

**Use Case:** Detect a cycle in a Linked List.
``` 
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def has_cycle(head):
    slow, fast = head, head
    while fast is not None and fast.next is not None:
        fast = fast.next.next
        slow = slow.next
        if slow == fast:
            return True  # Cycle detected
    return False

# Example
head = Node(1)
head.next = Node(2)
head.next.next = head # Cycle created
print(has_cycle(head)) # Output: True
```
### 3. Sliding Window

**Concept:** Expand a window (range) as long as a condition is met, then shrink it from the left to find 
the optimal contiguous subarray.

**When to use:** Input is a linear data structure and the problem asks for the longest/shortest substring, 
subarray, or a desired value.

**Use Case:** Maximum Sum Subarray of Size K.
```
def max_sub_array_of_size_k(k, arr):
    max_sum, window_sum = 0, 0
    window_start = 0

    for window_end in range(len(arr)):
        window_sum += arr[window_end]  # Add the next element
        
        # Slide the window, we don't need to slide if we've not hit the required window size of 'k'
        if window_end >= k - 1:
            max_sum = max(max_sum, window_sum)
            window_sum -= arr[window_start]  # Subtract the element going out
            window_start += 1  # Slide the window ahead
    return max_sum

# Example
print(max_sub_array_of_size_k(3, [2, 1, 5, 1, 3, 2])) # Output: 9 (Subarray [5, 1, 3])
```

### 4.Merge Intervals
**Concept:** Sort intervals by start time, then iterate to merge overlapping ones.

**When to use:** You have data representing ranges (time, numbers) and need to find overlaps or merge them.

**Use Case:** Merge overlapping intervals.
```
def merge_intervals(intervals):
    if len(intervals) < 2:
        return intervals
    
    # Sort by start time
    intervals.sort(key=lambda x: x[0])
    
    merged = []
    start = intervals[0][0]
    end = intervals[0][1]
    
    for i in range(1, len(intervals)):
        interval = intervals[i]
        if interval[0] <= end:  # Overlapping intervals, adjust the 'end'
            end = max(interval[1], end)
        else:  # Non-overlapping, add previous and reset
            merged.append([start, end])
            start = interval[0]
            end = interval[1]
    
    merged.append([start, end])
    return merged

# Example
print(merge_intervals([[1, 4], [2, 5], [7, 9]])) # Output: [[1, 5], [7, 9]]
```

### 5. Cyclic Sort

**Concept:** Iterate over the array and swap numbers to their correct indices
(index i should contain value i+1 or i).

**When to use:** Problems involving arrays containing numbers in a given range (e.g., 1 to N) and finding 
missing/duplicate numbers.

**Use Case:** Find the missing number in an array containing 0 to n.
```
def find_missing_number(nums):
    i, n = 0, len(nums)
    while i < n:
        j = nums[i]
        # If nums[i] is within bounds and not in correct position, swap
        if nums[i] < n and nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1
            
    # Find the first index missing its correct number
    for i in range(n):
        if nums[i] != i:
            return i
    return n

# Example
print(find_missing_number([4, 0, 3, 1])) # Output: 2
```

### 6. In-place Reversal of a Linked List

**Concept:** Reverse links one by one using a prev pointer to track the reversed portion.

**When to use:** You need to reverse a linked list (or a sub-part of it) without using extra memory (O(1) space).

**Use Case:** Reverse a Linked List.

```
def reverse(head):
    previous, current = None, head
    while current is not None:
        next_node = current.next  # Temporarily store the next node
        current.next = previous   # Reverse the current node
        previous = current        # Move previous to current
        current = next_node       # Move current to next
    return previous

# Example logic (assuming Node class exists and print helper)
# Input: 1 -> 2 -> 3 -> 4 -> 5 -> null
# Output: 5 -> 4 -> 3 -> 2 -> 1 -> null
```

### 7. Two Heaps

**Concept:** Maintain a Max Heap for the lower half of numbers and a Min Heap for the upper half to quickly access the median.

**When to use:** Priority Queue scheduling, finding the median of number streams, or finding the smallest/largest elements of two sets.

**Use Case:** Find the median of a number stream.
```
from heapq import *

class MedianFinder:
    def __init__(self):
        self.max_heap = []  # containing first half of numbers
        self.min_heap = []  # containing second half of numbers

    def add_num(self, num):
        if not self.max_heap or -self.max_heap[0] >= num:
            heappush(self.max_heap, -num)
        else:
            heappush(self.min_heap, num)

        # Rebalance heaps
        if len(self.max_heap) > len(self.min_heap) + 1:
            heappush(self.min_heap, -heappop(self.max_heap))
        elif len(self.max_heap) < len(self.min_heap):
            heappush(self.max_heap, -heappop(self.min_heap))

    def find_median(self):
        if len(self.max_heap) == len(self.min_heap):
            return (-self.max_heap[0] + self.min_heap[0]) / 2.0
        return -self.max_heap[0] / 1.0

# Example
mf = MedianFinder()
mf.add_num(3)
mf.add_num(1)
print(mf.find_median()) # Output: 2.0
mf.add_num(5)
print(mf.find_median()) # Output: 3.0
```

### 8. Modified Binary Search

**Concept:** Apply binary search logic but adapt the comparison to handle unsorted or shifted data.

**When to use:** Searching in sorted arrays, rotated sorted arrays, or infinite arrays.

**Use Case:** Order-agnostic Binary Search (find target regardless of Ascending/Descending sort).
```
def binary_search(arr, key):
    start, end = 0, len(arr) - 1
    is_ascending = arr[start] < arr[end]
    
    while start <= end:
        mid = start + (end - start) // 2
        if key == arr[mid]:
            return mid
        
        if is_ascending:
            if key < arr[mid]: end = mid - 1
            else: start = mid + 1
        else:
            if key > arr[mid]: end = mid - 1
            else: start = mid + 1
            
    return -1

# Example
print(binary_search([10, 6, 4], 10)) # Output: 0
print(binary_search([1, 2, 3, 4, 5], 4)) # Output: 3
```

### 9. Top 'K' Elements

**Concept:** Use a heap to track the 'K' most significant elements efficiently.

**When to use:** Finding the top/smallest/frequent 'K' elements in a set.

**Use Case:** Find the Kth largest element in a stream or array.
```
from heapq import *

def find_k_largest_numbers(nums, k):
    min_heap = []
    # Put first 'K' numbers in the min heap
    for i in range(k):
        heappush(min_heap, nums[i])
    
    # Go through the rest of the numbers
    for i in range(k, len(nums)):
        if nums[i] > min_heap[0]:
            heappop(min_heap)
            heappush(min_heap, nums[i])
            
    return list(min_heap)

# Example
print(find_k_largest_numbers([3, 1, 5, 12, 2, 11], 3)) # Output: [5, 12, 11] (Order varies)
```

### 10. K-way Merge

**Concept:** Use a Min Heap to merge K sorted lists. Track the smallest current element from each list.

**When to use:** You have K sorted arrays or lists and need to merge them or find the Kth smallest element across all of them.

**Use Case:** Merge K Sorted Lists.
```
from heapq import heappush, heappop

def merge_lists(lists):
    min_heap = []
    
    # Put the first element of each list in the min heap
    # Tuple format: (value, list_index, element_index)
    for i in range(len(lists)):
        if lists[i]: # Check if list is not empty
            heappush(min_heap, (lists[i][0], i, 0))
            
    result = []
    while min_heap:
        value, list_idx, element_idx = heappop(min_heap)
        result.append(value)
        
        # If the list has more elements, push the next one to heap
        if element_idx + 1 < len(lists[list_idx]):
            heappush(min_heap, (lists[list_idx][element_idx+1], list_idx, element_idx+1))
            
    return result

# Example
l1 = [2, 6, 8]
l2 = [3, 6, 7]
l3 = [1, 3, 4]
print(merge_lists([l1, l2, l3])) # Output: [1, 2, 3, 3, 4, 6, 6, 7, 8]
```

### 11. Topological Sort (Graph)

**Concept:** Determine the linear ordering of nodes based on dependencies using In-Degrees and a Queue (BFS).

**When to use:** Problems involving graphs with directed edges (dependencies), task scheduling, or detecting cycles in directed graphs.

**Use Case:** Course Schedule (Can you finish all courses given prerequisites?).from collections import deque
```
def can_finish_courses(num_courses, prerequisites):
    sorted_order = []
    if num_courses <= 0: return False

    # 1. Initialize graph and in_degree
    in_degree = {i: 0 for i in range(num_courses)}
    graph = {i: [] for i in range(num_courses)}

    # 2. Build the graph
    for parent, child in prerequisites:
        graph[parent].append(child)
        in_degree[child] += 1

    # 3. Find all sources (vertices with 0 in-degrees)
    sources = deque()
    for key in in_degree:
        if in_degree[key] == 0:
            sources.append(key)

    # 4. Sort
    while sources:
        vertex = sources.popleft()
        sorted_order.append(vertex)
        for child in graph[vertex]:
            in_degree[child] -= 1
            if in_degree[child] == 0:
                sources.append(child)

    # If sorted_order doesn't contain all courses, there is a cyclic dependency
    return len(sorted_order) == num_courses

# Example
# 2 courses. Course 0 must be taken before course 1.
print(can_finish_courses(2, [[0, 1]])) # Output: True
```

### 12. Subsets

**Concept:** Use a Breadth-First Search (BFS) approach or cascading to generate all possible permutations or combinations. Start with an empty set and iterate through input numbers, adding the current number to all existing subsets to create new ones.

**When to use:** Problems asking for all Permutations, Combinations, or the Power Set of a dataset.

**Use Case:** Find all distinct subsets of an array.
```
def find_subsets(nums):
    subsets = [[]]
    for current_number in nums:
        # Take all existing subsets and add the current number to them to create new subsets
        n = len(subsets)
        for i in range(n):
            # create a new subset from the existing subset and add the current element to it
            set_copy = list(subsets[i])
            set_copy.append(current_number)
            subsets.append(set_copy)
    return subsets

# Example
print(find_subsets([1, 5, 3])) 
# Output: [[], [1], [5], [1, 5], [3], [1, 3], [5, 3], [1, 5, 3]]
```

### 13. Greedy Techniques

**Concept:** At each step, choose the optimal immediate choice (local optimum) in the hope that it leads to the global optimum. 
Unlike DP, you do not reconsider previous choices.

**When to use:** Optimization problems where a local optimal choice leads to a global solution (e.g., Activity Selection, Minimum Coin Change with standard currency).

**Use Case:** Activity Selection (Find max non-overlapping activities).
```
def print_max_activities(activities):
    # Sort activities by their finish time
    activities.sort(key=lambda x: x[1])
    
    selected_activities = [activities[0]]
    last_finish_time = activities[0][1]
    
    for i in range(1, len(activities)):
        # If this activity starts after or when the last one finished
        if activities[i][0] >= last_finish_time:
            selected_activities.append(activities[i])
            last_finish_time = activities[i][1]
            
    return selected_activities

# Example: (start, end)
tasks = [(1, 4), (3, 5), (0, 6), (5, 7), (3, 8), (5, 9), (6, 10), (8, 11), (8, 12), (2, 13), (12, 14)]
print(print_max_activities(tasks)) 
# Output includes tasks like (1, 4), (5, 7), (8, 11), (12, 14)
```
### 14. Backtracking

**Concept:** Build a solution incrementally. If the current path fails to satisfy constraints, "backtrack" (undo the last step) and try a different path.

**When to use:** Constraint satisfaction problems (Sudoku, N-Queens, generating valid parentheses).

**Use Case:** Generate all Permutations.
```
def permute(nums):
    result = []
    
    # helper function
    def backtrack(path, remaining_nums):
        if not remaining_nums:
            result.append(path)
            return
        
        for i in range(len(remaining_nums)):
            # Pick one number, add to path, and backtrack with the rest
            backtrack(path + [remaining_nums[i]], 
                      remaining_nums[:i] + remaining_nums[i+1:])
            
    backtrack([], nums)
    return result

# Example
print(permute([1, 2, 3]))
# Output: [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
```

### 15. Dynamic Programming

**Concept:** Break a complex problem into simpler subproblems. Store the results of subproblems (Memoization) to avoid redundant calculations.

**When to use:** Problems with "Overlapping Subproblems" and "Optimal Substructure" (e.g., Fibonacci, Knapsack, Longest Common Subsequence).

**Use Case:** 0/1 Knapsack Problem.
```
def solve_knapsack(profits, weights, capacity):
    # dp[i][c] stores max profit for first 'i' items with capacity 'c'
    n = len(profits)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n)]

    # Initialize for the first item
    for c in range(capacity + 1):
        if weights[0] <= c:
            dp[0][c] = profits[0]

    for i in range(1, n):
        for c in range(1, capacity + 1):
            profit1, profit2 = 0, 0
            # Include the item, if it fits
            if weights[i] <= c:
                profit1 = profits[i] + dp[i-1][c-weights[i]]
            # Exclude the item
            profit2 = dp[i-1][c]
            dp[i][c] = max(profit1, profit2)

    return dp[n-1][capacity]

# Example
print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 7)) # Output: 22
```

### 16. Sort and Search

**Concept:** Sorting data often simplifies the problem, allowing the use of other techniques like Two Pointers or simple iteration to find duplicates/groups.

**When to use:** When inputs are arrays/strings and you need to group elements, find unique elements, or check for equality efficiently.

**Use Case:** Group Anagrams.
```
def group_anagrams(strs):
    anagram_map = {}
    
    for s in strs:
        # Sort the string to use as a key
        # "eat" -> "aet", "tea" -> "aet"
        sorted_str = "".join(sorted(s))
        
        if sorted_str in anagram_map:
            anagram_map[sorted_str].append(s)
        else:
            anagram_map[sorted_str] = [s]
            
    return list(anagram_map.values())

# Example
print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
# Output: [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
```

### 17. Matrices

**Concept:** Traverse a 2D array (grid) using rows and columns. Often involves modifying the grid in-place to mark visited nodes during DFS/BFS.

**When to use:** Graph problems represented as grids (islands, mazes).

**Use Case:** Number of Islands.
```
def num_islands(grid):
    if not grid: return 0
    count = 0
    rows, cols = len(grid), len(grid[0])
    
    def dfs(r, c):
        if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == '0':
            return
        grid[r][c] = '0' # Mark as visited (sink the island)
        dfs(r+1, c) # down
        dfs(r-1, c) # up
        dfs(r, c+1) # right
        dfs(r, c-1) # left

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1':
                count += 1
                dfs(r, c)
    return count

# Example
grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
print(num_islands(grid)) # Output: 3
```

### 18. Stacks

**Concept:** Last-In, First-Out (LIFO). Useful for tracking "open" operations that must be "closed" in reverse order.

**When to use:** Parsing strings, matching parentheses, evaluating expressions, or tracking previous "greater/smaller" elements.

**Use Case:** Valid Parentheses.
```
def is_valid(s):
    stack = []
    mapping = {")": "(", "}": "{", "]": "["}
    
    for char in s:
        if char in mapping:
            # Pop the topmost element; if stack is empty, use dummy value
            top_element = stack.pop() if stack else '#'
            if mapping[char] != top_element:
                return False
        else:
            stack.append(char)
            
    return not stack

# Example
print(is_valid("()[]{}")) # True
print(is_valid("(]"))     # False
```

### 19. Tree Depth First Search (DFS)

**Concept:** Recursively explore a tree by going as deep as possible along each branch before backtracking.

**When to use:** Tree problems involving path sums, height, or serialization.

**Use Case:** Path Sum (Check if root-to-leaf path equals target).
```
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def has_path_sum(root, target_sum):
    if not root:
        return False
    
    # If leaf node, check if value matches remaining sum
    if not root.left and not root.right:
        return target_sum == root.val
        
    return (has_path_sum(root.left, target_sum - root.val) or 
            has_path_sum(root.right, target_sum - root.val))

# Example
root = TreeNode(5)
root.left = TreeNode(4)
root.right = TreeNode(8)
root.left.left = TreeNode(11, TreeNode(7), TreeNode(2))
# Path 5 -> 4 -> 11 -> 2 equals 22
print(has_path_sum(root, 22)) # True
```

### 20. Trie (Prefix Tree)

**Concept:** A tree-like data structure used to efficiently store and retrieve keys in a dataset of strings.

**When to use:** Autocomplete, spell checker, or finding words with a common prefix.

**Use Case:** Insert and Search words.
```
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word

# Example
trie = Trie()
trie.insert("apple")
print(trie.search("apple"))   # True
print(trie.search("app"))     # False
```

### 21. Hash Maps

**Concept:** A collection of (key, value) pairs offering O(1) average time complexity for lookups, insertions, and deletions.

**When to use:** Fast lookups, counting frequencies, or mapping relationships.
**Use Case:** Two Sum (Find indices of two numbers adding to target).
```
def two_sum(nums, target):
   ``` prev_map = {}  # val : index
    
    for i, n in enumerate(nums):
        diff = target - n
        if diff in prev_map:
            return [prev_map[diff], i]
        prev_map[n] = i
    return []

# Example
print(two_sum([2, 7, 11, 15], 9)) # Output: [0, 1]
```

### 22. Knowing What to Track

**Concept:** Often the key to an efficient solution is simply tracking the frequency of elements (using a Hash Map or Array) or tracking a global state.

**When to use:** Palindrome problems (tracking odd counts), finding Majority elements, or Anagram validation.

**Use Case:** Longest Palindrome (Using character counts).
```
from collections import Counter

def longest_palindrome(s):
    counts = Counter(s)
    length = 0
    has_odd = False
    
    for count in counts.values():
        if count % 2 == 0:
            length += count
        else:
            length += count - 1
            has_odd = True
            
    return length + 1 if has_odd else length

# Example
# "abccccdd" -> one "a", one "b", four "c"s, two "d"s.
# We can use 4 "c"s + 2 "d"s + 1 (either "a" or "b") = 7
print(longest_palindrome("abccccdd")) # Output: 7
```

### 23. Union Find (Disjoint Set)
**Concept:** A data structure that keeps track of elements partitioned into disjoint (non-overlapping) sets. It supports 'union' (merge sets) and 'find' (determine which set an element is in).

**When to use:** Network connectivity, finding connected components in a graph, or detecting cycles in an undirected graph.

**Use Case:** Count Connected Components.
```
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.count = n # Initially n disjoint components

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x]) # Path compression
        return self.parent[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            self.parent[rootX] = rootY
            self.count -= 1

# Example
# 5 nodes: 0, 1, 2, 3, 4. Edges: (0, 1), (1, 2), (3, 4)
uf = UnionFind(5)
uf.union(0, 1)
uf.union(1, 2)
uf.union(3, 4)
print(uf.count) # Output: 2 (Component {0,1,2} and {3,4})
```