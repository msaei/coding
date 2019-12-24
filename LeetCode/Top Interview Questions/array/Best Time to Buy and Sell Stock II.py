#Best Time to Buy and Sell Stock II
#https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/564/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        for i in range(len(prices)-1):
            if prices[i]<prices[i+1]:
                ans+=prices[i+1]-prices[i]
        return ans 
