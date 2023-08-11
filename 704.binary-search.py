#
# @lc app=leetcode id=704 lang=python3
#
# [704] Binary Search
#

# @lc code=start
# class Solution:
    # def search(self, nums: [int], target: int) -> int:
    #     length = len(nums)
    #     array = nums
    #     i = length // 2
    #     while len(array) > 0:
    #         if array[i] == target:
    #             index = nums.index(array[i])
    #             return index
    #         elif array[i] < target:
    #             array = array[i:]
    #             i = i // 2
    #         else: # array[i] > target
    #             array = array[:i]
    #             i = i // 2
    #     return -1
class Solution:
    def search(self, nums: [int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = l + ((r - l) // 2)  # (l + r) // 2 can lead to overflow
            if nums[m] > target:
                r = m - 1
            elif nums[m] < target:
                l = m + 1
            else:
                return m
        return -1


# @lc code=end
payload = {
    'self': None,
    'nums': [-1,0,3,5,9,12],
    'target': 9,
}
Solution.search(**payload)