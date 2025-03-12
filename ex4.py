import heapq
import random

class Heap:
    def __init__(self):
        self.heap = []
        
    def heapify(self, arr):
        """Initialize the internal array and rearrange it into a min heap."""
        self.heap = arr.copy()
        n = len(self.heap)
        for i in range(n // 2 - 1, -1, -1):
            self._heapify_down(i)
    
    def _heapify_down(self, i):
        """Ensures the sub-tree rooted at index i is a valid min heap."""
        n = len(self.heap)
        smallest = i
        left = 2 * i + 1
        right = 2 * i + 2
        
        if left < n and self.heap[left] < self.heap[smallest]:
            smallest = left
        if right < n and self.heap[right] < self.heap[smallest]:
            smallest = right
        if smallest != i:
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            self._heapify_down(smallest)
    
    def enqueue(self, element):
        """Add an element to the heap while maintaining the heap property."""
        self.heap.append(element)
        self._heapify_up(len(self.heap) - 1)
    
    def _heapify_up(self, i):
        """Bubbles the element at index i upward to restore heap order."""
        parent = (i - 1) // 2
        if i > 0 and self.heap[i] < self.heap[parent]:
            self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
            self._heapify_up(parent)
    
    def dequeue(self):
        """
        Remove and return the root element from the heap.
        Returns None if the heap is empty.
        """
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        
        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return root


# Tests


def test_heapify_sorted():
    """Test with an input array that is already a correctly sorted (min heap) array."""
    arr = [1, 2, 3, 4, 5, 6, 7]
    h = Heap()
    h.heapify(arr)
    
    expected = arr.copy()
    heapq.heapify(expected)
    
    assert h.heap == expected, f"Test failed: Expected {expected}, got {h.heap}"
    print("test_heapify_sorted passed")

def test_heapify_empty():
    """Test with an empty input array."""
    arr = []
    h = Heap()
    h.heapify(arr)
    
    expected = []
    assert h.heap == expected, f"Test failed: Expected {expected}, got {h.heap}"
    print("test_heapify_empty passed")

def test_heapify_random():
    """Test with a long, randomly shuffled list of integers."""
    arr = list(range(1, 21)) 
    random.shuffle(arr)
    h = Heap()
    h.heapify(arr)
    
    expected = arr.copy()
    heapq.heapify(expected)
    
    assert h.heap == expected, f"Test failed: Expected {expected}, got {h.heap}"
    print("test_heapify_random passed")

if __name__ == "__main__":
    test_heapify_sorted()
    test_heapify_empty()
    test_heapify_random()
    
    print("\nExample usage of enqueue and dequeue:")
    h = Heap()
    h.heapify([10, 15, 20])
    print("Initial heap:", h.heap)
    h.enqueue(5)
    print("Heap after enqueue(5):", h.heap)
    removed = h.dequeue()
    print("Dequeued element:", removed)
    print("Heap after dequeue:", h.heap)
