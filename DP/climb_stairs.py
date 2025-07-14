class Solution:
    def climbStairs(self, n: int) -> int:
        cache = [-1] * n
        def stairs(i):
            if i >= n:
                return i == n
            if cache[i] != -1:
                return cache[i]
            cache[i] = stairs(i + 1) + stairs(i + 2)
            return cache[i]
        
        return stairs(0)
        
          