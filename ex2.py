import timeit
import random

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert_recursive(self.root, key)

    def _insert_recursive(self, root, key):
        if root is None:
            return Node(key)
        if key < root.key:
            root.left = self._insert_recursive(root.left, key)
        else:
            root.right = self._insert_recursive(root.right, key)
        return root

    def search(self, key):
        return self._search_recursive(self.root, key)

    def _search_recursive(self, root, key):
        if root is None or root.key == key:
            return root
        if key < root.key:
            return self._search_recursive(root.left, key)
        return self._search_recursive(root.right, key)


def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def measure_performance():
    elements = list(range(10000))
    random.shuffle(elements)
    
    bst = BinarySearchTree()
    for elem in elements:
        bst.insert(elem)
    
    total_bst_time = 0
    for elem in elements:
        avg_time = timeit.timeit(lambda: bst.search(elem), number=10) / 10
        total_bst_time += avg_time
    
    avg_bst_time_per_search = total_bst_time / len(elements)
    print(f"BST - Average search time: {avg_bst_time_per_search:.10f} seconds")
    print(f"BST - Total search time: {total_bst_time:.10f} seconds")
    
    elements.sort()
    
    total_binary_search_time = 0
    for elem in elements:
        avg_time = timeit.timeit(lambda: binary_search(elements, elem), number=10) / 10
        total_binary_search_time += avg_time
    
    avg_binary_search_time_per_search = total_binary_search_time / len(elements)
    print(f"Binary Search - Average search time: {avg_binary_search_time_per_search:.10f} seconds")
    print(f"Binary Search - Total search time: {total_binary_search_time:.10f} seconds")

if __name__ == "__main__":
    measure_performance()


'''
    4.) Binary search on the array is faster than the binary search tree. This is because the binary search tree
        has an average time complexity of O(log n) for searching, while the binary search on the array has a time
        complexity of O(log n) as well. However, the binary search tree has more individual tasks to complete in the time
        complexity, which causes it to be slower than the binary search on the array. The binary search tree has
        to traverse the tree and compare the keys at each node, while the binary search on the array only needs to
        compare the key at the middle of the array. This makes the binary search on the array faster than the binary
        search tree. In summary, a BST search is slower than binary search because of pointer-based tree traversal and 
        possible unbalanced structures.
'''