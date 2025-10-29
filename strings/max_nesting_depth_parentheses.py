class Solution:
    def maxDepth(self, s: str) -> int:
        max_depth = 0
        open_count = 0

        for ch in s:
            if ch == "(":
                open_count += 1
                max_depth = max(open_count, max_depth)
            elif ch == ")":
                open_count -= 1
        return max_depth