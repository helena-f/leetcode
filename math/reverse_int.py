class Solution:
    def reverse(self, x: int) -> int:
        new = 0
        negative_flag = False
        if x < 0:
            negative_flag = True
            x = x * -1
        
        while x > 0:
            digit = x % 10
        
            new = new * 10 + digit
            if new > 2**31 -1:
                return 0
            x = x // 10

        return -1 * new if negative_flag else new