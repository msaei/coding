#Factorial Trailing Zeroes
#https://leetcode.com/explore/interview/card/top-interview-questions-medium/113/math/816

class Solution:
    def trailingZeroes(self, n: int) -> int:
        fives = 0
        while n >0:
            n = n // 5
            fives += n
        return fives
