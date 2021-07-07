class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        M = len(grid)
        if M == 0:
            return 0
        N = len(grid[0])
        if N == 0:
            return 0

        def visit(grid, i, j):
            area = 1
            grid[i][j] = 0
            if i+1 < M and grid[i+1][j]:
                area += visit(grid, i+1, j)
            if i > 0 and grid[i-1][j]:
                area += visit(grid, i-1, j)
            if j+1 < N and grid[i][j+1]:
                area += visit(grid, i, j+1)
            if j > 0 and grid[i][j-1]:
                area += visit(grid, i, j-1)
            return area

        max_area = 0
        for i in range(M):
            for j in range(N):
                if grid[i][j]:
                    max_area = max(max_area, visit(grid,i,j))
        

        return max_area