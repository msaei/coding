#Search a 2D Matrix II
#https://leetcode.com/explore/interview/card/top-interview-questions-medium/110/sorting-and-searching/806

class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        rows = len(matrix)
        if rows == 0: return False
        cols = len(matrix[0])
        i = 0
        j = cols - 1
        while (i < rows and j > -1):
            if matrix[i][j] > target:
                j -= 1
            elif matrix[i][j] < target:
                i += 1
            else:
                return True
        return False
        
