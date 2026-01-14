class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        # which recursive calls make duplicate subsets
        # [1,2,1,1]
        # [1,1,1,2]

        res = []

        subarray = []
        def dfs(i):
            if i >= len(nums):
                res.append(subarray[:])
                return

            # either take elt
            subarray.append(nums[i])
            dfs(i+1)

            # or not
            subarray.pop()

            while i + 1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
            dfs(i+1)
        dfs(0)
        return res