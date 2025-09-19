class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs (i,arr, arrsum):
            # condition to add: currsum = target
            if arrsum == target:
                res.append(arr.copy())
                return
            # base case: end of arr or currsum > target
            if i >= len(nums) or arrsum > target:
                return

            # recursion: include another copy of self
            arr.append(nums[i])
            arrsum += nums[i]
            dfs(i, arr, arrsum)
            arr.pop()
            # include next number
            arrsum -= nums[i]
            dfs(i+1, arr, arrsum)

        dfs(0,[], 0)
        return res