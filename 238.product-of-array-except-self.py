#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#

# @lc code=start
from functools import reduce
# class Solution:
#     def productExceptSelf(self, nums: [int]) -> [int]:
#         result = []
#         for i, n in enumerate(nums):
#             print(nums[:i])
#             print(nums[i+1:])
#             mulitplying_array = nums[:i] + nums[i+1:]
#             answer = 1
#             for item in mulitplying_array:
#                 answer = answer * item
#             result.append(answer)
#         return result


class Solution:
    def productExceptSelf(self, nums: [int]) -> [int]:
        res = [1] * (len(nums))
        prefix = 1
        array = range(len(nums))
        for i in array:
            res[i] = prefix
            prefix *= nums[i]
        postfix = 1
        _array = range(len(nums) - 1, -1, -1)
        for i in _array:
            res[i] *= postfix
            postfix *= nums[i]
        return res
    
# payload = [1,2,3,4]
# result = Solution.productExceptSelf(Solution, payload)
# print('================', result)

# ChatGPTより
# 今回の具体的な例である range(len(nums) - 1, -1, -1) は、nums リストの長さから1引いた値から、- 1まで（- 1は含まれない）を1ずつ減らすことで、リストの要素を逆順にアクセスするためのインデックスのシーケンスを生成しています。

# 配列の引数のインデックスを扱うときはrangeを使うことが多い！

# @lc code=end

