#String to Integer
#https://leetcode.com/explore/featured/card/top-interview-questions-easy/127/strings/884/

class Solution:
    def myAtoi(self, stri: str) -> int:
        res = 0
        i = 0
        sign = 1
        l = len(stri)
        while i<l and stri[i] == ' ':
            i += 1
            
        if i >= l:
            return 0
        
        if stri[i] == '-':
            sign = -1
            i += 1
        elif stri[i] == '+':
            i += 1
            
        if i >= l:
            return 0
        
        nums = '0123456789'
        while i<l and stri[i] in nums:
            res = res * 10 + nums.find(stri[i])
            i += 1
            
        res *= sign
        INT_MIN = - (2 ** 31)
        INT_MAX = 2 ** 31 -1
        if res < INT_MIN:
            return INT_MIN
        if res > INT_MAX:
            return INT_MAX
        return res
