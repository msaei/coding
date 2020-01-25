#Longest Increasing Subsequence
#https://leetcode.com/explore/interview/card/top-interview-questions-medium/111/dynamic-programming/810/


class Solution:
    def binarySearch(self, nums, key):
        right = len(nums) - 1
        left = 0
        
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == key:
                return mid
            if nums[mid] < key:
                left = mid + 1
            else:
                right = mid - 1
        
        return -left -1

    def lengthOfLIS(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        dp = [nums[0]]
        for num in nums:
            i = self.binarySearch(dp, num)
            if i < 0:
                i = -i - 1
            if i == len(dp):
                dp.append(num)
            else:
                dp[i] = num
        print(dp)
        return len(dp)
        
        
        
    def lengthOfLIS_n2(self, nums: List[int]) -> int:
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
