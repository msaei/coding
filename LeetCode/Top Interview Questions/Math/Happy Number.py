#Happy Number
#https://leetcode.com/explore/interview/card/top-interview-questions-medium/113/math/815/


class Solution:
    def isHappy(self, n: int) -> bool:
        nums = []
        while True:
            acc = 0
            while n > 0:
                a = n % 10
                n = n // 10
                acc += a ** 2
            print(acc)    
            if acc == 1:
                return True
            if acc in nums:
                return False
            nums.append(acc)
            n = acc
