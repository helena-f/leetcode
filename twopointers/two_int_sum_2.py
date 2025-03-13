

# Two Integer Sum II
# Given an array of integers numbers that is sorted in non-decreasing order.

# Return the indices (1-indexed) of two numbers, [index1, index2], such that they add up to a given target number target and index1 < index2. Note that index1 and index2 cannot be equal, therefore you may not use the same element twice.

# There will always be exactly one valid solution.

# Your solution must use 
# O
# (
# 1
# )
# O(1) additional space.

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        left = 0 
        right = len(numbers) - 1

        currsum = 0
        while right > left:
            print(left, right)
            currsum = numbers[left] + numbers[right]
            print(currsum)
            if currsum == target:
                return [left+1,right+1]
            if currsum < target:
                left += 1
            if currsum > target:
                right -=1
        return []
            


