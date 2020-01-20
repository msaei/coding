#Abstract Painting
#https://open.kattis.com/problems/abstractpainting

def getCombinations(rows: int, cols: int) -> int:
    if rows * cols == 0:
        return 0
    a = (rows - 1) + (cols - 1)
    b = (rows - 1) * (cols - 1)
    return (18 * (6 ** a) * (2 ** b)) % 1000000007

n = int(input())
for _ in range(n):
    r,c = map(int, input().split())
    print(getCombinations(r,c))

