class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # start with the most frequent elements left: hashmap -> heapify
        # q: how to iterate through order of elements
        # a: go through cycle of elements to interweve; each task has the same cooldown
        # so if the cycle length of the remaining elts is less than n, add idle
        # since its letters, the size is a constant limited by 27 

        # cases
        # XYYY, n = 1 -> Y X Y idle Y -> 5

        # algorithm:
        # 1. iterate through tasks and count freq with hashmap
        #       key = task[i], val = freq
        # 2. heapify the map by frequency left, for max-heap
        # 3. start with the max heap. pop the most frequent elt
        # 4. push the freq left and the time it's available to the end of the queue
        # 5. if the 1st elt of queue is available then add to max heap

        # step 1: 
        cmap = {}
        for task in tasks:
            if task in cmap:
                # want max heap
                cmap[task] -= 1
            else:
                cmap[task] = -1

        # step 2:
        heap = list(cmap.values())
        heapq.heapify(heap)

        # step 3:
        time = 0
        q = deque()
        while heap or q:
            time += 1

            if heap:
                prev = heapq.heappop(heap)
                freq_left = prev + 1
                if freq_left != 0:
                    q.append([freq_left, time + n])
                
            else:
                time = q[0][1]

            if q and q[0][1] == time:
                heapq.heappush(heap, q[0][0])
                q.popleft()

        return time