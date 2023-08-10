#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#

# @lc code=start
class Solution:
    def maxArea(self, height: [int]) -> int:
        res = 0
        l = 0
        r = len(height) -1
        while l < r:
            w = r - l
            h = min(height[l], height[r])
            area = h * w
            res = max(res, area)
            if height[l] < height[r]:
                l += 1
            elif height[l] > height[r]:
                r -= 1
            else:
                l += 1
        return res


# @lc code=end

