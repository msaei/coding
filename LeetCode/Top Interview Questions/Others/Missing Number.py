#Missing Number
#https://leetcode.com/explore/interview/card/top-interview-questions-easy/99/others/722/

class Solution:
    def missingNumber1(self, nums: List[int]) -> int:
        l = len(nums)
        expected = l * (l + 1) // 2
        total = sum(nums)
        return expected - total
    
    def missingNumber(self, nums: List[int]) -> int:
        l = len(nums)
        res = l
        for i in range(l):
            res = res + i - nums[i]
        return res
        
