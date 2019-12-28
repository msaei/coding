#Valid Anagram
#https://leetcode.com/explore/featured/card/top-interview-questions-easy/127/strings/882/

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
