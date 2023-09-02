#
# @lc app=leetcode id=33 lang=python3
#
# [33] Search in Rotated Sorted Array
#

# @lc code=start
class Solution:
    def search(self, nums: [int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if target == nums[m]:
                return m

            if nums[l] <= nums[m]:
                if nums[l] > target or nums[m] < target:
                    l = m + 1
                else:
                    r = m - 1
            else:
                if nums[r] < target or nums[m] > target:
                    r = m - 1
                else:
                    l = m + 1
        return -1
# @lc code=end

Solution.search(None, [4,5,6,7,0,1,2], 0)