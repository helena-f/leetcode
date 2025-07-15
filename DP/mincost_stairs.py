class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        n = len(cost)
        cache = [-1] * n
        def stair(i):
            if i >= n:
                return 0

            if cache[i] != -1:
                return cache[i]

            cache[i] = cost[i] + min(stair(i+1), stair(i+2))
            return cache[i]
        return min(stair(0),stair(1))