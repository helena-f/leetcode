class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m = {}
        for i in s1:
            if i in m:
                m[i] = m[i] + 1
            else:
                m[i] = 1
        n = len(s1)

        
        for i in range(len(s2) - n + 1):
            h = m.copy()
            match_count = 0
            for j in range(i, i+n):
                
                if s2[j] in h and h[s2[j]] != 0:
                    h[s2[j]] -= 1
                    match_count += 1
                else:
                    break
            if match_count == n:
                    return True  
                
            

        return False
