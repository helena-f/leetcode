class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str

        394 leetcode
        """
        def dfs(i):
            res = ""
            while i < len(s) and s[i] != ']':
                # series of alpha to append
                if not s[i].isalpha():
                    # get full number to multiply by
                    num = 0
                    while s[i].isdigit():
                        num = num * 10 + int(s[i]) 
                        i += 1

                    # next must be a bracket
                    i += 1
                    # deal with nested brackets
                    subseq, i = dfs(i)
                    i += 1

                    res += subseq * num
                else: 
                    res += s[i]
                    i += 1
                    
                    
            return res, i

        return dfs(0)[0]