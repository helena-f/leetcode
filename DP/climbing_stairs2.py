class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        cost1 = 0
        cost2 = costs[0] + 1
        cost3 = costs[1] + min(cost2 + 1, 4) if n > 1 else cost2
        for i in range(2, n):
            curr = min(costs[i] + 1 + cost3,
                       costs[i] + 4 + cost2,
                       costs[i] + 9 + cost1) 

            cost1 = cost2
            cost2 = cost3
            cost3 = curr

        return cost3

        # memo = {}
        # def dp(i):
        #     if i >= n:
        #         return 0
            
        #     if i in memo:
        #         return memo[i]

        #     cost1 = costs[i] + 1 + dp(i+1)
        #     cost2 = costs[i + 1] + 4 + dp(i+2) if i + 2 <= n else float("inf")
        #     cost3 = costs[i + 2] + 9 + dp(i+3) if i + 3 <= n else float("inf")
        #     memo[i] = min(cost1, cost2, cost3)
        #     return memo[i]
        
        # return dp(0)