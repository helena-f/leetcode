class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        if not nums:
            return []

        arr = []
        def backtrack( i):
            # out of bounds
            if i >= len(nums):
                res.append(arr.copy())
                return
            
            # include nums[i]
            arr.append(nums[i])
            backtrack(i+1)

            # don't include nums[i]
            arr.pop()
            backtrack(i+1)
            
        backtrack( 0)
        return res
# (very very slow)
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        if not nums:
            return []

        def backtrack(curr, nums):
           
            for i in range(len(nums)):
                curr.append(nums[i])
                res.append(curr[:])
                backtrack(curr, nums[1+i:])
                curr.pop()

        
        arr = []
        backtrack(arr, nums)
        res.append([])
        return res