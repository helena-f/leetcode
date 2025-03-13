
import heapq

class KthLargest:
    
    def __init__(self, k, nums):
        self.minHeap, self.k = nums, k
        heapq.heapify(self.minHeap)
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        return self.minHeap[0]
    
kthLargest = KthLargest(3, [1, 2, 3, 3])
print(kthLargest.add(3))  
print(kthLargest.add(5))  
print(kthLargest.add(6))  
print(kthLargest.add(7))  
print(kthLargest.add(8))    
