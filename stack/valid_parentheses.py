# Valid Parentheses
# You are given a string s consisting of the following characters: '(', ')', '{', '}', '[' and ']'.

# The input string s is valid if and only if:

# Every open bracket is closed by the same type of close bracket.
# Open brackets are closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
# Return true if s is a valid string, and false otherwise.
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        st = []
        m = {')': '(', '}':'{',']':'['}
        
        for i in s:
            if i in m.values():
                st.append(i)
            
            elif i in m:
                if not st or m[i] != st.pop():
                    return False
        return (len(st) == 0)
        
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        bracketmap = {'(':')', '[': ']', '{': '}'}
        for ch in s:
            if ch in bracketmap:
                stack.append(ch)
            
            print(stack)
            if ch in bracketmap.values():
                if len(stack) == 0:
                    return False
                else:
                    stackchar = stack.pop()
                if bracketmap[stackchar] != ch:
                    return False
        if len(stack) != 0:
            return False
        return True
            
        class Solution:
    def isValid(self, s: str) -> bool:
        bracket_map = {")":"(", "}":"{", "]": "["}

        stack = []

        for ch in s:
            if ch in bracket_map.values():
                stack.append(ch)
            elif not stack or stack.pop() != bracket_map[ch]:
                return False
        if len(stack) != 0:
            return False
        return True