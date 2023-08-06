#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        import re

        def remove_non_alphabetic(input_str):
            result_str = re.sub(r'[^a-zA-Z0-9]', '', input_str)
            return result_str
        _s = remove_non_alphabetic(s).lower()
        print(_s)
        if len(_s) <= 1:
            return True
        half_l = len(_s) // 2
        for i in range(half_l):
            if _s[i] == _s[(-i) -1]:
                continue
            return False
        return True


# @lc code=end
Solution.isPalindrome(None, "race a car"
)

# non-alphanumeric
# numericが数字