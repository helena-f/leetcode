class Solution:
    def reorganizeString(self, s: str) -> str:
        # cases:
        # "" -> ""
        # aaabs -> abas

        # notes:
        # greedy approach; most frequent char is used -> max heap
        # need a cooldown component
        # impossible if more than half of the string is 1 char

        # algorithm:
    
        # 1. create hashmap of ch and their frequencies
        # 2. build max heap
        # 3. check if impossible
        # 4. track previous char. while heap: 
        #       a) pop the most frequent ch, add to result
        #       b) if the previous has frequency left, push it back to the heap
        #       c) update previous to the popped, freq + 1 
        # 5. return result

        # step 1
        counts = Counter(s)

        # step 2
        heap = [(-freq, ch) for ch, freq in counts.items()]
        heapq.heapify(heap)

        # step 3
        if max(counts.values()) > (len(s) + 1) // 2:
            return ""

        # step 4 
        res = []
        prev = (0, "")
        while heap:
            freq, ch = heapq.heappop(heap)
            res.append(ch)
            if prev[0] != 0:
                heapq.heappush(heap, prev)
            
            prev = (freq + 1, ch)
        
        return "".join(res)


