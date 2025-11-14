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


        class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # costs build on each other
        # either step to the next floor or 2 floors above
        # decision: step to the floor that costs less
        # if there's a tie, pick the further one

        # cases: 
        # [2, 3, 5, 3] -> 2 + 5  = 7
        # [2, 3, 3, 4] -> 2 + 3 = 5
        # [1,2,1,2,1,1,1] -> 1 + 1 + 1 + 1
        if len(cost) == 1:
            return cost[0]
        min_1 = 0
        min_2 = 0

        for i in range(len(cost)):
            temp = min(min_1 + cost[i], min_2 + cost[i])
            min_1 = min_2
            min_2 = temp

        return min( min_1, min_2)