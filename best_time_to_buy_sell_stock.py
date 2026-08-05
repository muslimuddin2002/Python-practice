# LeetCode: Best Time to Buy and Sell Stock
# Given an array of prices, find the maximum profit from buying on one
# day and selling on a later day. Uses a sliding window (two pointers).

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        maxP = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
            else:
                l = r
            r += 1
        return maxP
