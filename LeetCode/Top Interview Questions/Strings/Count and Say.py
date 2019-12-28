#Count and Say
#https://leetcode.com/explore/featured/card/top-interview-questions-easy/127/strings/886/

class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return '1'
        s = self.countAndSay(n -1)
        i = 0
        c = 0
        cur = s[0]
        res = ""
        while i < len(s):
            if cur == s[i]:
                c += 1
                i += 1
            else:
                res += str(c)
                res += str(cur)
                cur = s[i]
                c = 0
                
        res += str(c)
        res += str(cur)
        return res

