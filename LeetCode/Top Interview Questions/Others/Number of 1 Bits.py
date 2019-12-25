#Number of 1 Bits
#https://leetcode.com/explore/interview/card/top-interview-questions-easy/99/others/565/

class Solution:
    def hammingWeight(self, n: int) -> int:
        #return str(bin(n))[2:].count('1')
        counter = 0
        while n > 0:
            n &= n-1
            counter += 1
        return counte
        
