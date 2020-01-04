#Climbing Stairs
#https://leetcode.com/explore/featured/card/top-interview-questions-easy/97/dynamic-programming/569/

class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 4:
            return n
        prev = 1
        cur = 2
        for _ in range(n-2):
            temp = cur + prev
            prev = cur
            cur = temp
        return cur
