#Longest Increasing Subsequence
#https://leetcode.com/explore/interview/card/top-interview-questions-medium/111/dynamic-programming/810/

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        
        dp = [0] * n
        dp[0] = 1
        maxans = 1
        for i in range(1, n):
            curmax = 0 
            for j in range(i):
                if nums[i] > nums[j]:
                    curmax = max(curmax, dp[j])
            dp[i] = curmax + 1
            maxans = max(maxans, dp[i])
        return maxans
