#Number of Islands
#https://leetcode.com/explore/interview/card/top-interview-questions-medium/108/trees-and-graphs/792/

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def eraseCell(i : int, j : int) -> None:
            if i<0 or j<0 or j>=cols or i >= rows or grid[i][j]=='0':
                return
            grid[i][j] = '0'
            eraseCell(i, j+1)
            eraseCell(i, j-1)
            eraseCell(i-1, j)
            eraseCell(i+1, j)
            return
        
        rows = len(grid)
        if rows == 0:
            return 0
        cols = len(grid[0])
        count = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    count += 1
                    eraseCell(i, j)
        return count
