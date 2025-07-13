class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        size = len(s)
        pals = [[False] * size for _ in range(size) ] 
        res = 0
        for i in range(size-1, -1, -1):
            for j in range(i, size):
                if s[i] == s[j] and (j-i <= 2 or pals[i+1][j-1]):
                    pals[i][j] = True
                    res += 1
        return res
