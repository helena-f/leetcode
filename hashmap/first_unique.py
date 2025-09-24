class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        m = {}
        for ch in range(len(s)):
            if s[ch] in m:
                m[s[ch]] += 1
            else:
                m[s[ch]] = 1
        
        for i in range(len(s)):
            if m[s[i]] == 1:
                return i

        return -1