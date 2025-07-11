# Given a string s, return true if it is a palindrome, otherwise return false.

# A palindrome is a string that reads the same forward and backward. It is also case-insensitive and ignores all non-alphanumeric characters.

class Solution:
    import re
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r'\W+', '', s).lower()
        print(s)
        left, right = 0,0

        size = len(s)
        if size % 2 == 0:
            left = int(size/2) -1
            right = int(size/2)
        else:
            left = right = int(size/2)

        print(left, right)

        while left >= 0 and right < size:
            if s[left] != s[right]:
                print(s[left], s[right])
                return False
            left -= 1
            right += 1
        return True
    
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = ''.join(c.lower() for c in s if c.isalnum())
        mid = len(s) // 2
        tail = len(s) 

        for i in range(mid):  
            tail -= 1    
            if s[i] != s[tail]:
                return False
        
        return True