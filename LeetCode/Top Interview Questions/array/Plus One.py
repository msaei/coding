#Plus One
#https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/559/

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        i = -1
        while carry > 0:
            digits[i] += 1
            carry = 0
            if digits[i] == 10:
                digits[i] = 0
                carry = 1
            if i == -len(digits) and carry == 1:
                return [1] + digits[:]
            i -= 1
        return digits[:]
