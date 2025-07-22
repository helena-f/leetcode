class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        memo = [-1] * n

        def combo(i):
            
            if i >= n:
                return 1
            
            if memo[i] != -1:
                return memo[i]

            if s[i] == "0":
                return 0
            
            res = combo(i+1)
            if (i + 1 < n and (s[i] == '1' or s[i] == '2' and s[i+1] in "0123456")) :
                res += combo(i+2)
            memo[i] = res
            return memo[i]
        
        return combo(0)