#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#


# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        brackets_pair = {")": "(", "]": "[", "}": "{"}
        stack = []

        for c in s:
            if c not in brackets_pair:
                stack.append(c)
            else:
                if not stack or stack[-1] !=brackets_pair[c]:
                    return False
                else:
                    stack.pop()
        return not stack



# @lc code=end
