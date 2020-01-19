#House Robber
#https://leetcode.com/explore/featured/card/top-interview-questions-easy/97/dynamic-programming/576/

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        res=0
        dp0 = nums[0]
        dp1 = max(nums[0], nums[1])
        for i in range(2, n):
            res = max(dp1, dp0 + nums[i])
            dp0 =dp1
            dp1 = res
        return dp1
    
    def rob_mem(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, n):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        return dp[n-1]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
