#Unique Paths
#https://leetcode.com/explore/interview/card/top-interview-questions-medium/111/dynamic-programming/808

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        mem = [[1] * n for _ in range(m)]
        print(mem)
        for i in range(1, m):
            for j in range(1, n):
                mem[i][j] = mem[i-1][j]+mem[i][j-1]
        print(mem)
                
        return mem[m-1][n-1]
