#Reverse Bits
#https://leetcode.com/explore/interview/card/top-interview-questions-easy/99/others/648/

class Solution:
    def reverseBits(self, n: int) -> int:
        res = str(bin(n))[2:]
        n = 32 - len(res)
        res = res[::-1]
        res += '0' * n
        return int(res, 2)
        
