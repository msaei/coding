#Longest Palindromic Substring
#https://leetcode.com/explore/interview/card/top-interview-questions-medium/103/array-and-strings/780/

class Solution:
    
    def longestPalindrome(self, s: str) -> str:
        
        def isPalindrome(word: str) -> bool:
            return word == word[::-1]
        
        l = len(s)
        while l > 0:
            for i in range(len(s) - l + 1):
                if isPalindrome(s[i:i + l]):
                    return s[i:i+l]
            l -= 1
            
        return ''
