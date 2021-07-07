class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        M = len(grid)
        N = len(grid[0])
        steps = 0

        queue = []
        for m in range(M):
            for n in range(N):
                if grid[m][n] == 2:
                    queue.append((m,n))
        queue.append((-1,-1))
                    

        while queue:
            m,n = queue.pop(0)
            if m==-1 and n==-1:
                steps+=1
                if queue:
                    queue.append((-1,-1))
            else:
                if m<M-1 and grid[m+1][n] == 1:
                    grid[m+1][n] = 2
                    queue.append((m+1,n))
                if m>0 and grid[m-1][n] == 1:
                    grid[m-1][n] = 2
                    queue.append((m-1,n))
                if n<N-1 and grid[m][n+1] == 1:
                    grid[m][n+1] = 2
                    queue.append((m,n+1))
                if n>0 and grid[m][n-1] == 1:
                    grid[m][n-1] = 2
                    queue.append((m,n-1))
                    
        for m in range(M):
            for n in range(N):
                if grid[m][n] == 1:
                    return -1
        if steps > 0:
            return steps-1
        else:
            return steps
'''
[[2,1,1],[1,1,0],[0,1,1]]
[[2,1,1],[0,1,1],[1,0,1]]
[[1]]
[[0]]
[[1],[2],[2]]
[[2],[2]]
[[0],[2]]
[[2,2,2,1,1]]
'''