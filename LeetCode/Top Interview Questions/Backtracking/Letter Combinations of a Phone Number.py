#Letter Combinations of a Phone Number
#https://leetcode.com/explore/interview/card/top-interview-questions-medium/109/backtracking/794/

# recursive solution
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digMap = { '2': "abc", '3':"def", '4':"ghi", '5':"jkl", '6':"mno", '7':"pqrs", '8':"tuv", '9':"wxyz"}
        if len(digits) == 0:
            return []
        if len(digits) == 1:
            return [a for a in digMap[digits[0]]]
        res = []
        previus = self.letterCombinations(digits[1:])
        for l in digMap[digits[0]]:
            res += [l+x for x in previus]
        return res
    
# bachtracking
class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        phone = {'2': ['a', 'b', 'c'],
                 '3': ['d', 'e', 'f'],
                 '4': ['g', 'h', 'i'],
                 '5': ['j', 'k', 'l'],
                 '6': ['m', 'n', 'o'],
                 '7': ['p', 'q', 'r', 's'],
                 '8': ['t', 'u', 'v'],
                 '9': ['w', 'x', 'y', 'z']}
                
        def backtrack(combination, next_digits):
            # if there is no more digits to check
            if len(next_digits) == 0:
                # the combination is done
                output.append(combination)
            # if there are still digits to check
            else:
                # iterate over all letters which map 
                # the next available digit
                for letter in phone[next_digits[0]]:
                    # append the current letter to the combination
                    # and proceed to the next digits
                    backtrack(combination + letter, next_digits[1:])
                    
        output = []
        if digits:
            backtrack("", digits)
        return output

    
