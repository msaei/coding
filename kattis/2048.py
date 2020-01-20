#2048
#https://open.kattis.com/problems/2048

def transform(nums):
    res = [0] * 4
    nums = list(nums)
    nums.append(-1) # trick to add a fake number to compare to
    p1 = 0
    p2 = 1
    pr = 0
    while p2 < 5:
        if nums[p1] == 0:
            p1 += 1
            p2 += 1
            continue
        if nums[p2] == 0:
            p2 += 1
            continue
        if nums[p1] == nums[p2]:
            res[pr] = nums[p1] * 2
            pr += 1
            p1 += 2
            p2 += 2
        else:
            res[pr] = nums[p1]
            pr += 1
            p1 += 1
            p2 += 1
    return res

def rotate(board):
    return list(zip(*board))

def move(board, direction):
    if direction in ['1', '3']:
        board = rotate(board)
        
    for i in range(4):
        if direction in ['0', '1']:
            board[i] = transform(board[i][:]) #left up
        else:
            board[i] = transform(board[i][::-1])[::-1] #right down
    if direction in ['1', '3']:
        board = rotate(board)
    return board
        

def showBoard(board):
    for row in board:
        print(*row)
        

grid = []
for _ in range(4):
    grid.append(list(map(int, input().split())))
dir = input()

newGrid = move(grid, dir)
showBoard(newGrid)


