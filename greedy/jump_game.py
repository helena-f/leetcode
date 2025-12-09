class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums) - 1
        for i in range(n-1, -1, -1):
            if i + nums[i] >= n:
                n = i
        return n == 0

        # memo = {}
        # def dp(i):
        #     if i in memo:
        #         return memo[i]
        #     if i >= len(nums) - 1:
        #         return True
        #     if nums[i] == 0:
        #         return False

        #     end = min(len(nums), i + nums[i] + 1)

        #     for j in range(i + 1, end):
        #         if dp(j):
        #             memo[i] = True
        #             return True
        #     memo[i] = False
        #     return False
        # return dp(0)