#Rotate Image
#https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/770/

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        i = 0
        j = 0
        while i < n//2:
            while j < n/2:
                r = i
                c = j
                source = matrix[r][c]
                for _ in range(4):
                    dr = c
                    dc = n - 1 - r
                    print(r, c, dr, dc)
                    source , matrix[dr][dc] = matrix[dr][dc], source
                    r = dr
                    c = dc
                j += 1
            i += 1
            j = 0
