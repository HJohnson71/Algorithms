# Merging sorted sublist using min-heap: O(nlogk)

import heapq
def sort(A):
    heap = [(sublist[0], sublist, 1) for sublist in A if sublist]
    heapq.heapify(heap)
    output = []
    while heap:
        value, sublist, index = heapq.heappop(heap)
        output.append(value)
        if index < len(sublist):
            next_value = sublist[index]
            heapq.heappush(heap, (next_value, sublist, index + 1))
    return output

# Test:

print(sort([[1]])) # returns [1]
print(sort([[2], [1]])) # returns [1, 2]
print(sort([[2, 3, 3, 4], [1, 5], [1, 2, 4]])) # returns [1, 1, 2, 2, 3, 3, 4, 4, 5]
print(sort([[10, 100], [1, 1, 1], [1, 1000]])) # returns [1, 1, 1, 1, 10, 100, 1000]

# Kth largest element across sublist using max-heap: O(klogk)

def k_largest(A, k):
    heap = [(sublist[0], sublist, 1) for sublist in A if sublist]
    heapq.heapify(heap)
    kth_largest = None
    floor = 0
    while heap and floor < k:
        max_value, sublist, index = heapq.heappop(heap)
        kth_largest = max_value
        if index > 0:
            prev_value = sublist[index - 1]
            heapq.heappush(heap, (prev_value, sublist, index - 1))
        floor += 1
    if floor < k or not kth_largest:
        return None
    return kth_largest

# Test:

print(k_largest([[1]], 1)) # returns 1
print(k_largest([[2], [1]], 2))# returns 1
print(k_largest([[2, 3, 3, 4], [1, 5], [1, 2, 4]], 4)) # returns 3
print(k_largest([[10, 100], [1, 1, 1], [1, 1000]], 7)) # returns 1

# Kth largest element of Binary Search Tree: O(log^2(n))

class Node:
    def __init__(self, key: int):
        self.left = None
        self.right = None
        self.value = key
def count_nodes(root: Node):
    if root is None:
        return 0
    return 1 + count_nodes(root.left) + count_nodes(root.right)
def k_largest_bst(root: Node, k: int):
    n = count_nodes(root)
    if k <= 0 or k > n:
        return None
    test = root
    while test:
        right_nodes = count_nodes(test.right)
        if right_nodes + 1 == k:
            return test
        if right_nodes >= k:
            test = test.right
        else:
            k -= right_nodes + 1
            test = test.left
    return None
