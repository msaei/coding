#Reverse Integer
#https://leetcode.com/explore/featured/card/top-interview-questions-easy/127/strings/880/

class Solution:
    def reverse(self, x: int) -> int:
        res = 0
        sign = 1
        if x < 0:
            sign = -1
            x = -1 * x
        while x > 0:
            d = x % 10 
            x = x // 10
            res = res * 10 + d
        res = res * sign
        limit = 2 ** 31
        if res >= (limit -1) or res <= -1 * limit:
            return 0
        return res
