import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = nums[:]
        heapq.heapify(self.heap)
        self.k = k

        # min heap, where you keep the k largest elements with the kth being at the top
        i = len(nums)
        while i > k:
            heapq.heappop(self.heap)
            i -= 1

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        
        return self.heap[0]