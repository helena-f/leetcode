
# Evaluate Reverse Polish Notation
# Solved 
# You are given an array of strings tokens that represents a valid arithmetic expression in Reverse Polish Notation.

# Return the integer that represents the evaluation of the expression.

# The operands may be integers or the results of other operations.
# The operators include '+', '-', '*', and '/'.
# Assume that division between integers always truncates toward zero.
# Example 1:

# Input: tokens = ["1","2","+","3","*","4","-"]

# Output: 5

# Explanation: ((1 + 2) * 3) - 4 = 5
# Constraints:

# 1 <= tokens.length <= 1000.
# tokens[i] is "+", "-", "*", or "/", or a string representing an integer in the range [-100, 100].



class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        value = 0
        
        operands = {'+': 1, '-': 2, '*':3, '/':4}

        for i in tokens:
            if i not in operands:
                stack.append(int(i))
            else:
                if stack:
                    val2 = stack.pop()
                    val1 = stack.pop()
                    if operands[i] == 1:
                        stack.append(val1 + val2)
                    elif operands[i] == 2:
                        stack.append(val1 - val2)
                    elif operands[i] == 3:
                        stack.append(val1 * val2)
                    else:
                        stack.append(int(val1 / val2))
        return stack.pop()