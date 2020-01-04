#Maximum Subarray
#https://leetcode.com/explore/featured/card/top-interview-questions-easy/97/dynamic-programming/566/

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        accum = min (0, nums[0] - 1)
        maxSum = accum

        for n in nums:
            if accum + n < n:
                accum = n
            else:
                accum += n
                
            if accum > maxSum:
                maxSum = accum
        return maxSum
