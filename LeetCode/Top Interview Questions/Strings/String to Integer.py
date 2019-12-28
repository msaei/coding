#Implement strStr
#https://leetcode.com/explore/featured/card/top-interview-questions-easy/127/strings/885/

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        h = len(haystack)
        n = len(needle)
        if n == 0:
            return 0
        
        for i in range(h - n + 1):

            if needle == haystack[i:i+n]:
                return i
        return -1
