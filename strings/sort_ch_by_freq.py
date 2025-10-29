# Time Complexity : O(n)
class Solution:
    def frequencySort(self, s: str) -> str:
        freqs = Counter(s)
        
        res = [(-freq,ch) for ch, freq in freqs.items()]
        
        heapq.heapify(res)

        new = []
        while res:
            curr = heapq.heappop(res)
            new.append(curr[1] * (curr[0] * -1))
      
        return "".join(new)
# Time Complexity : O(n log n)
class Solution:
    def frequencySort(self, s: str) -> str:
        freqs = Counter(s)
        
        res = [(freq,ch) for ch, freq in freqs.items()]
        res.sort(reverse = True)
        
        new = [ch * freq for freq, ch in res]
      
        return "".join(new)