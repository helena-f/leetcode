class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s
        
        longest = []
        longest_len = -1
        
        
        for i in range(len(s)):
            #odd
            left, right = i, i

            while left >= 0 and right < len(s) and s[left] == s[right]:

                if (right - left + 1) > longest_len:
                    longest = s[left:right+1]
                    longest_len = (right - left + 1)

                left -= 1
                right += 1

            left, right = i, i+1
            while left >= 0 and right < len(s) and s[left] == s[right]:

                if (right - left + 1) > longest_len:
                    longest = s[left:right+1]
                    longest_len = (right - left + 1)

                left -= 1
                right += 1
            

        return longest