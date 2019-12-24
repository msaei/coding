#Roman to Integer
#https://leetcode.com/explore/interview/card/top-interview-questions-easy/102/math/878/

class Solution:
    def romanToInt(self, s: str) -> int:
        vals = { "I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000 \
                   , "IV":4, "IX":9, "XL":40, "XC":90, "CD":400, "CM":900 }
        i = 0
        l = len(s)
        res = 0
        while i < l:
            if i+1 < l and s[i:i+2] in vals.keys():
                symb = s[i:i+2]
                res += vals[symb] 
                i += 2
            else:
                symb = s[i]
                res += vals[symb]
                i += 1
        return res
        
