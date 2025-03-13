# Binary Search
# You are given an array of distinct integers nums, sorted in ascending order, and an integer target.

# Implement a function to search for target within nums. If it exists, then return its index, otherwise, return -1.

# Your solution must run in 
# O
# (
# l
# o
# g
# n
# )
# O(logn) time.

# Example 1:

# Input: nums = [-1,0,2,4,6,8], target = 4

# Output: 3
# Example 2:

# Input: nums = [-1,0,2,4,6,8], target = 3

# Output: -1

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)
        m = 0

        while left < right:
            m = int((left + right ) / 2)
            if nums[m] == target:
                return m
            
            if nums[m] > target:
                right = m
            if nums[m] < target:
                left = m+1

        return -1