class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        remove = [False] * len(s)

        stack = []

        for i, ch in enumerate(s):
            if ch == "(":
                stack.append([i, ch])
            elif ch == ")":
                if not stack:
                    remove[i] = True
                    continue

                index, op = stack.pop()
                if op != "(":
                    remove[index] = True
                    remove[i] = True
        while stack:
            index, op = stack.pop()
            remove[index] = True

        res = []
        for i in range(len(remove)):
            if not remove[i]:
                res.append(s[i])
        return "".join(res)