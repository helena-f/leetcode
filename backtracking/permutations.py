class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def dfs(i):
            # base case
            if i == len(nums):
                return [[]]
            
            # subproblem
            prev_call = dfs(i+1)
            curr = []
            for perm in prev_call:
                for j in range(len(perm)+1):
                    new = perm[:]
                    new.insert(j, nums[i])
                    curr.append(new)
            return curr

        
        return dfs(0)
