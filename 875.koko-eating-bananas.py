#
# @lc app=leetcode id=875 lang=python3
#
# [875] Koko Eating Bananas
#
import math
# @lc code=start


class Solution:
    def minEatingSpeed(self, piles: [int], h: int) -> int:
        l, r = 1, max(piles)
        res = max(piles)
        while l <= r:
            k = (l + r) // 2
            hours = 0
            for p in piles:
                hours += math.ceil(p / k)
            if hours <= h:
                res = min(res, k)
                r = k - 1
            else:
                l = k + 1
        return res
# @lc code=end
payload = {
    'self': None,
    'piles': [3,6,7,11],
    'h': 8
}
Solution.minEatingSpeed(**payload)

#バナナを1時間あたりに食べる個数の選択肢は有限
#→配列として捉え、二分探索法で特定する流れ