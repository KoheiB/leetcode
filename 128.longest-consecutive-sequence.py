#
# @lc app=leetcode id=128 lang=python3
#
# [128] Longest Consecutive Sequence
#

# @lc code=start
class Solution:
    def longestConsecutive(self, nums: [int]) -> int:
        # sorted_array = sorted(nums)
        # print(sorted_array)
        # max_count = 0
        # count = 0
        # for i, item in enumerate(sorted_array):
        #     print(i, item)
        #     if i+1 < len(sorted_array):
        #         if sorted_array[i+1] - item == 1:
        #             count += 1
        #         else:
        #             if count > max_count:
        #                 max_count = count
        #             count = 0
        # return max_count+1

        nums_set = set(nums)
        max_count = 0
        print(nums_set)

        for num in nums_set:
            if num - 1 not in nums_set:  # 最初の数を見つける
                current_num = num
                count = 1

                while current_num + 1 in nums_set:  # 連続した数を数える
                    current_num += 1
                    count += 1

                max_count = max(max_count, count)  # 最長の連続部分列を更新

        return max_count
# @lc code=end
