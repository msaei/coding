#Pascals Triangle
#https://leetcode.com/explore/interview/card/top-interview-questions-easy/99/others/601/

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        res = [[1]]
        prevRow = [1]
        for i in range(1, numRows):
            #generateNextRow(prevRow)
            nextRow = self.generateNextRow(prevRow)
            res.append(nextRow)
            prevRow = nextRow
        return res
            
            
            
    def generateNextRow(self, prevRow: List[int]) -> List[int]:
        if prevRow == None:
            return [1]
        l = len(prevRow) + 1
        res = [1] * l
        for i in range(l-2):
            res[i+1] = prevRow[i] + prevRow[i+1]
        return res
        
