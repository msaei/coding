#Set Matrix Zeroes
#https://leetcode.com/explore/interview/card/top-interview-questions-medium/103/array-and-strings/777

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        cols = len(matrix[0])
        rowMap = [1] * rows
        colMap = [1] * cols
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    rowMap[i] = 0
                    colMap[j] = 0
        for i in range(rows):
            for j in range(cols):
                matrix[i][j] *= rowMap[i] * colMap[j]
        return
        
