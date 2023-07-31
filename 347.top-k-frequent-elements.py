#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#

# @lc code=start
class Solution:
    def topKFrequent(self, nums: [int], k: int) -> [int]:
        n_dict = {}  # number => count
        for n in nums:
            if n in n_dict:
                n_dict[n] += 1
            else:
                n_dict[n] = 1
        sorted_items = sorted(
            n_dict.items(), key=lambda item: item[1], reverse=True)
        result_dict = dict(sorted_items[:k])
        return result_dict
# @lc code=end
