#
# @lc app=leetcode id=153 lang=python3
#
# [153] Find Minimum in Rotated Sorted Array
#

# @lc code=start
class Solution:
    def findMin(self, nums: [int]) -> int:
        # l, r = 0, len(nums) - 1
        # while l <= r:
        #     m = int(l + (r-l)/2)
        #     if nums[m] > nums[m + 1]:
        #         if m == len(nums) - 1:
        #             return nums[0]
        #         return nums[m+1]
        #     elif nums[m] < nums[l]:
        #         r -= 1
        #     else:
        #         l += 1
        # return nums[0]
        res = nums[0]
        l, r = 0, len(nums) - 1
        while l <= r:
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break
            m = (l + r ) // 2
            res = min(res, nums[m])
            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m -1
        return res

# @lc code=end
payload = {
    'self': None,
    'nums': [11,13,15,17]

}
Solution.findMin(**payload)