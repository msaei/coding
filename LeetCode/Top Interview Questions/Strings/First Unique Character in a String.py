#First Unique Character in a String
#https://leetcode.com/explore/featured/card/top-interview-questions-easy/127/strings/881/

class Solution:
    def firstUniqChar(self, s: str) -> int:
        counter = {}
        for c in s:
            if c in counter.keys():
                counter[c] += 1
            else:
                counter[c] = 1
        for i in range(len(s)):
            if counter[s[i]] == 1:
                return i
        return -1
