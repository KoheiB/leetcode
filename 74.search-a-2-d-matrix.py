#
# @lc app=leetcode id=74 lang=python3
#
# [74] Search a 2D Matrix
#

# @lc code=start
class Solution:
    def searchMatrix(self, matrix: [[int]], target: int) -> bool:
        flattened = [element for row in matrix for element in row]
        l, r = 0, len(flattened) -1
        while l <= r:
            m = l + ((r - l) // 2)  # (l + r) // 2 can lead to overflow
            if flattened[m] > target:
                r = m - 1
            elif flattened[m] < target:
                l = m + 1
            else:
                return True
        return False

# @lc code=end

