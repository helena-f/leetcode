
# Given an integer array nums, return an array output where output[i] is the product of all the elements of nums except nums[i].

# Each product is guaranteed to fit in a 32-bit integer.

# Follow-up: Could you solve it in 
# O
# (
# n
# )
# O(n) time without using the division operation?

# Example 1:

# Input: nums = [1,2,4,6]

# Output: [48,24,12,8]
# Example 2:

# Input: nums = [-1,0,1,2,3]

# Output: [0,-6,0,0,0]
# Constraints:

# 2 <= nums.length <= 1000
# -20 <= nums[i] <= 20


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix, suffix = [],[]
        prefix_total = 1
        suffix_total = 1

        if not nums:
            return []

        size = len(nums)
        for i in range(size):
            suffix_index = size - i - 1
            
            prefix_total = nums[i] * prefix_total
            prefix.append(prefix_total)

            suffix_total = nums[suffix_index] * suffix_total
            suffix.append(suffix_total)

        suffix.reverse()

        print(prefix)
        print(suffix)
        output = []
        for i in range(size):
            total_mult = 1
            print("finding for index: ", i)
            if i-1 >= 0:
                total_mult *= prefix[i-1]
                print("prefix ", prefix[i-1])
            if i+1 < size:
                total_mult *= suffix[i+1]
                print("suffix ",suffix[i+1])

            output.append(total_mult)

        return output
