#Longest Substring Without Repeating Characters
#https://leetcode.com/explore/interview/card/top-interview-questions-medium/103/array-and-strings/779

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        positions = {}
        left = -1
        right = 0
        max_len = 0
        
        while right < len(s):
            cur = s[right]
            
            if cur in positions.keys() and positions[cur] > left:
                left = positions[cur] 
                positions[cur] = right
            else:
                positions[cur] = right
                max_len = max(max_len, (right - left))
                
            right += 1
        return max_len
