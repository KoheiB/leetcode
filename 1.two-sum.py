#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
# class Solution:
#     def twoSum(self, nums: [int], target: int) -> [int]:
#         for i, num in enumerate(nums):
#             searching_value = target - num
#             for _i, _num in enumerate(nums):
#                 if _i == i:
#                     continue
#                 if _num == searching_value:
#                     return [i, _i]
class Solution:
    def twoSum(self, nums: [int], target: int) -> [int]:
        prevMap = {}  # val -> index

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i

        #[1, 3, 4, 5, 6], 10
        # {
        #     1:0,
        #     3:1,
        #     4:2,
        #     5:3,
        #     6:　→４ある！
        # }
        # return [prevMap[4], i=4]


# @lc code=end
