class Solution:
    def largestGoodInteger(self, num: str) -> str:
        m = -1
        for i in range(0, len(num) - 2):
            if num[i] == num[i + 1] == num[i + 2]:
                m = max(m, int(num[i]))
        
        return str(m) * 3 if m != -1 else ""