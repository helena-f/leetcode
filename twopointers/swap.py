class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # cases:
        # [1], 1 -> [1], 0
        # [1,2,3], 1 -> [2,3,1], 2
        # [1,2,3,1], 1 -> [2,3,1,1], 2

        # left = end of list where non target 
        # right = start of target value list

        # when find val, swap l and r
        # if r is val, don't swap. move r down until it is not val


        l, r = 0, len(nums) - 1

        while l <= r:
            if nums[l] == val:
                nums[l], nums[r] = nums[r], nums[l]
                r -= 1
            else:
                l += 1
        return l
        
        
        

