#Best Time to Buy and Sell Stock
#https://leetcode.com/explore/featured/card/top-interview-questions-easy/97/dynamic-programming/572/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0
        buy = prices[0]
        maxProfit = 0
        for p in prices:
            if p < buy:
                buy = p
            elif (p - buy) > maxProfit:
                maxProfit = p - buy
        return maxProfit
