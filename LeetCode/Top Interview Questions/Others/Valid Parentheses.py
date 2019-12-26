#Valid Parentheses
#https://leetcode.com/explore/interview/card/top-interview-questions-easy/99/others/721/

class Solution:
    def isValid(self, s: str) -> bool:
        bracks = {'(':')', '[':']', '{':'}'}
        stack = []
        for c in s:
            if c in bracks.keys():
                stack.append(bracks[c])
            else:
                if len(stack) == 0 or stack[-1] != c:
                    return False
                else:
                    stack.pop()
        return len(stack) == 0
        
