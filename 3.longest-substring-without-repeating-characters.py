#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # result = ""
        # _s = ""
        # l, r = 0, 1
        # if len(s) == 1:
        #     return 1
        # while r < len(s):
        #     if len(_s) == 0:
        #         _s += s[l]
        #     if s[r] not in _s:
        #         _s += s[r]
        #         r += 1
        #         if len(_s) > len(result):
        #             result = _s
        #     else:
        #         if len(_s) > len(result):
        #             result = _s
        #         _s = ""
        #         l += 1
        #         r = l + 1
        # return len(result)
        charSet = set()
        l = 0
        res = 0
        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, r-l+1)
        return res

# @lc code=end


payload = {
    'self': None,
    's': "au"
}
Solution.lengthOfLongestSubstring(**payload)
