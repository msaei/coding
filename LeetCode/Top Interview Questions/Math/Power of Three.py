#Power of Three
#https://leetcode.com/explore/interview/card/top-interview-questions-easy/102/math/745/

class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0
        isPrime = [True] * n
        counter = 0
        for i in range(2, n):
            if isPrime[i]:
                counter += 1
            else:
                continue
            for j in range(i, n, i):
                isPrime[j] = False
        return counter
        
