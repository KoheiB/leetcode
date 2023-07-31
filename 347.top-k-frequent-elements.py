#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#

# @lc code=start
# class Solution:
#     def topKFrequent(self, nums: [int], k: int) -> [int]:
#         n_dict = {}  # number => count
#         for n in nums:
#             if n in n_dict:
#                 n_dict[n] += 1
#             else:
#                 n_dict[n] = 1
#         sorted_items = sorted(
#             n_dict.items(), key=lambda item: item[1], reverse=True)
#         result_dict = dict(sorted_items[:k])
#         return result_dict

class Solution:
    def topKFrequent(self, nums: [int], k: int) -> [int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]
        print(freq)

        for n in nums:
            count[n] = 1 + count.get(n, 0)
        for n, c in count.items():
            freq[c].append(n)
        print(freq)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                print(res)
                if len(res) == k:
                    return res

        # O(n)

# @lc code=end
