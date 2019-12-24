#Valid Sudoku
#https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/769/

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #check rows
        for row in board:
            celDict = {}
            for cell in row:
                if cell in celDict.keys():
                    return False
                elif cell != '.':
                    celDict[cell] = 1
        #check columns
        
        for i in range(9):
            celDict = {}
            for j in range(9):
                cell = board[j][i]
                if cell in celDict.keys():
                    print(cell)
                    return False
                elif cell != '.':
                    celDict[cell] = 1
        #check squares
        
        corners = [(0,0) , (0,3), (0, 6), (3, 0), (3, 3), (3, 6), (6, 0), (6, 3), (6, 6)]
        for a, b in corners:
            celDict = {}
            for i in range(3):
                for j in range(3):
                    cell = board[i + a][j + b]
                    if cell in celDict.keys():
                        print(cell)
                        return False
                    elif cell != '.':
                        celDict[cell] = 1
        return True
