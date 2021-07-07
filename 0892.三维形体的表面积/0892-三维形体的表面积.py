class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        M = len(grid)
        if M == 0:
            return 0
        N = len(grid[0])
        if N == 0:
            return 0
        a = 0

        
        #print(a)
        for m in range(M):
            for n in range(N):
                if grid[m][n]:
                    a += (2 + grid[m][n]*4)
                if m>0 and grid[m-1][n]:
                    a -= 2*min(grid[m][n], grid[m-1][n])
                if n >0 and grid[m][n-1]:
                    a -= 2*min(grid[m][n], grid[m][n-1])

        return a
'''
[[2]]
[[1,2],[3,4]]
[[1,0],[0,2]]
[[1,1,1],[1,0,1],[1,1,1]]
[[2,2,2],[2,1,2],[2,2,2]]
'''