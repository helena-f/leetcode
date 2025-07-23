class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        m = set(s1)
        n = len(s1)

        
        l, r = 0, n
        while r <= len(s2):
            if set(s2[l:r]) == m:
                return True
            l+=1
            r+=1

        return False
