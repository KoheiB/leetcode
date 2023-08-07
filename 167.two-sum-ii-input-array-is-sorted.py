#
# @lc app=leetcode id=167 lang=python3
#
# [167] Two Sum II - Input Array Is Sorted
#

# @lc code=start
# class Solution:
#     def twoSum(self, numbers: [int], target: int) -> [int]:
#         l, r = 0, len(numbers) - 1
#         while l < r:
#             while l < r and numbers[l] + numbers[r] < target:
#                 l += 1
#             while l < r and numbers[l] + numbers[r] > target:
#                 r -= 1
#             if numbers[l] + numbers[r] == target:
#                 return [l + 1, r + 1]
class Solution:
    def twoSum(self, numbers: [int], target: int) -> [int]:
        l, r = 0, len(numbers) - 1

        while l < r:
            curSum = numbers[l] + numbers[r]

            if curSum > target:
                r -= 1
            elif curSum < target:
                l += 1
            else:
                return [l + 1, r + 1]


# @lc code=end


Solution.twoSum(None, [3, 24, 50, 79, 88, 150, 345], 200)
