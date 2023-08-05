#
# @lc app=leetcode id=150 lang=python3
#
# [150] Evaluate Reverse Polish Notation
#

# @lc code=start
class Solution:
    def evalRPN(self, tokens: [str]) -> int:
        stack = []
        for token in tokens:
            if token.isdigit() or (token[0] == '-' and token[1:].isdigit()):
                stack.append(int(token))
                continue
            else:
                b = stack.pop()
                a = stack.pop()
                if token == "+":
                    stack.append(a + b)
                elif token == "-":
                    stack.append(a - b)
                elif token == "*":
                    stack.append(a * b)
                elif token == "/":
                    # 切り捨て除算を行う
                    stack.append(int(a / b))
        return stack[0]
# @lc code=end
input = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]


Solution.evalRPN(None, input)
