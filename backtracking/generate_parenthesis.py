class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # n pairs of parenthesis
        res = []
        # generate all pairs brute force
        def dfs(op, close, subset):
            if op == n and close == n:
                res.append(subset)
                return
            if op < n:
                dfs(op + 1, close, subset + '(')
            if close < op:
                dfs(op, close + 1, subset + ')')
        dfs(0, 0, "")
        return res
