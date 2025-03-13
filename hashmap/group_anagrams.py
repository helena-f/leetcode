# Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.

# An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

# Example 1:

# Input: strs = ["act","pots","tops","cat","stop","hat"]

# Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]
# Example 2:

# Input: strs = ["x"]

# Output: [["x"]]
# Example 3:

# Input: strs = [""]

# Output: [[""]]
# Constraints:

# 1 <= strs.length <= 1000.
# 0 <= strs[i].length <= 100
# strs[i] is made up of lowercase English letters.


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anagram_groups = []
        anagram_indices = {}
        for string in strs:
            sorted_string = str(sorted(string))
            index_to_insert = anagram_indices.get(sorted_string, len(anagram_indices))
            anagram_indices[sorted_string] = index_to_insert

            if len(anagram_indices) > len(anagram_groups):
                anagram_groups.append([string])
            else:
                anagram_groups[index_to_insert].append(string)
        
        return anagram_groups

