#Jump Game
#https://leetcode.com/explore/interview/card/top-interview-questions-medium/111/dynamic-programming/807/

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        mem = [0] * n
        mem[n - 1] = 1
        p = n -1
        for i in range(n-2, -1, -1):
            if (i + nums[i]) >= p:
                mem[i] = 1
                p = i
            else:
                mem[i] = -1
            
        
        return mem[0] == 1
