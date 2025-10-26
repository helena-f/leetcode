class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        # cases:
        # "" -> ""
        # "()()" -> ""
        # "((()())(" -> "(()())"
        # "(()())(())" -> "()()()"
        # remark- outtermost if opens/closes completely before another open
    
        no_outer = []
        op = 0
        
        for ch in s:
            
            if ch == "(":
                if op != 0:
                    no_outer.append(ch)
                op += 1
            else:
                if op != 1:
                    no_outer.append(ch)
                op -= 1


        return "".join(no_outer)
            