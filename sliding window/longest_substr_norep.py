# Longest Substring Without Repeating Characters
# Solved 
# Given a string s, find the length of the longest substring without duplicate characters.

# A substring is a contiguous sequence of characters within a string.

# Example 1:

# Input: s = "zxyzxyz"

# Output: 3
# Explanation: The string "xyz" is the longest without duplicate characters.

# Example 2:

# Input: s = "xxxx"

# Output: 1
# Constraints:

# 0 <= s.length <= 1000
# s may consist of printable ASCII characters.


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxlen = 0
        currlen = 0

        left = right = 0
        while right < len(s) and left < len(s):
            # print(left,right)
            if s[right] not in s[left:right]:
                right += 1
                currlen += 1
                print(currlen)
                maxlen = max(currlen, maxlen)
            else: 
                left += 1
                currlen -= 1

        return maxlen