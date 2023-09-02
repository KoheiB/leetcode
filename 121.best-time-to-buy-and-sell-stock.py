#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: [int]) -> int:
        # l, r = 0, 1
        # max_profit = 0
        # while r < len(prices):
        #     if prices[l] < prices[r]:
        #         profit = prices[r] - prices[l]
        #         max_profit = max(max_profit, profit)
        #     else:
        #         l = r
        #     r += 1
        # return max_profit
        min_price = float('inf')
        max_profit = 0
        for price in prices:
            if price < min_price:
                min_price = price
            elif price-min_price > max_profit:
                max_profit = price-min_price
        return max_profit



# @lc code=end
Solution.maxProfit(None, [7,1,5,3,6,4])