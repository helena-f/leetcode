class Solution:
    def decodeString(self, s: str) -> str:
        curr_string = ""
        stack = []

        i = 0
        num = 0
        while i < len(s):
            if s[i].isdigit():
                num = num * 10 + int(s[i])
            elif s[i] == "[":
                stack.append([num, curr_string])
                curr_string = ""
                num = 0
            elif s[i] == "]":
                mult, prev_string = stack.pop()
                curr_string = prev_string+ mult * curr_string
            else:
                curr_string += s[i]
            i += 1
        return curr_string

