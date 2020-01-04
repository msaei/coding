#Word Search
#https://leetcode.com/explore/interview/card/top-interview-questions-medium/109/backtracking/797/

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])

        starting_points = []
        s = word[0]

        for row in range(rows):
            for col in range(cols):
                if board[row][col] == s:
                    starting_points.append([row, col])

        if len(starting_points) == 0:
            return False

        def is_valid(x, y, m, letter):

            # check bounds
            if not ((x > -1) and (y > -1) and (x < rows) and (y < cols)):
                return False

            # check if letter is valid
            return board[x][y] == letter and m[x][y]

        def find_word(x, y, m, curr_word):

            if curr_word == "":
                return True

            if is_valid(x, y, m, curr_word[0]):

                m[x][y] = False

                if find_word(x+1, y, m, curr_word[1:]) or \
                       find_word(x-1, y, m, curr_word[1:]) or \
                       find_word(x, y+1, m, curr_word[1:]) or \
                       find_word(x, y-1, m, curr_word[1:]):
                    return True

                m[x][y] = True
                return False

        for x, y in starting_points:
            m = [[True for _ in range(cols)] for _ in range(rows)]
            if find_word(x, y, m, word):
                return True

        return False
