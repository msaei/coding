#Hamming Distance
#https://leetcode.com/explore/interview/card/top-interview-questions-easy/99/others/762/

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        #return str(bin(x ^ y))[2:].count('1')
        c = 0
        n = x ^ y
        while n>0:
            n &= n - 1
            c += 1
        return c
        
