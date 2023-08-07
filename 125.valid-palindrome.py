#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#

# @lc code=start
# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         import re

#         def remove_non_alphabetic(input_str):
#             result_str = re.sub(r'[^a-zA-Z0-9]', '', input_str)
#             return result_str
#         _s = remove_non_alphabetic(s).lower()
#         print(_s)
#         if len(_s) <= 1:
#             return True
#         half_l = len(_s) // 2
#         for i in range(half_l):
#             if _s[i] == _s[(-i) -1]:
#                 continue
#             return False
#         return True
class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            while l < r and not self.alphanum(s[l]):
                l += 1
            while l < r and not self.alphanum(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True

    # Could write own alpha-numeric function
    def alphanum(self, c):
        return (
            ord("A") <= ord(c) <= ord("Z")
            or ord("a") <= ord(c) <= ord("z")
            or ord("0") <= ord(c) <= ord("9")
        )


# @lc code=end
Solution.isPalindrome(None, "race a car"
)

# non-alphanumeric
# numericが数字