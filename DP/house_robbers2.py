class Solution:
    def rob(self, nums: List[int]) -> int:
        # whether robbing 1 to n to 0 to n-1
        if len(nums) == 1:
            return nums[0]

        def dp(start,end):
            rob1 = 0
            rob2 = 0

            for i in range(start, end):
                temp = max(nums[i] + rob1, rob2)
                rob1 = rob2
                rob2 = temp
            
            return rob2

        return max(dp(0, len(nums) -1), dp(1, len(nums)))