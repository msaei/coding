#Longest Common Prefix
#https://leetcode.com/explore/featured/card/top-interview-questions-easy/127/strings/887/

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        if len(strs) == 0:
            return ""
        i = 0
        while True:
            if i >= len(strs[0]):
                return res

            cur = strs[0][i]    
            for j in range(1, len(strs)):
                if len(strs[j]) <= i or strs[j][i] != cur:
                    return res
                
            i += 1
            res += cur

