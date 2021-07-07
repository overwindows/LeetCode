class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        land = []
        ocean = []

        M = len(grid)
        if M == 0:
            return -1
        N = len(grid[0])
        if N == 0:
            return -1
        assert M == N
        for m in range(M):
            for n in range(N):
                if grid[m][n] == 1:
                    land.append([m,n])
                else:
                    ocean.append([m,n])
        if len(ocean) == 0 or len(land) == 0:
            return -1
        
        Q = []
        for x,y in land:
            if x>0 and grid[x-1][y] == 0:
                grid[x-1][y] = -1
                Q.append([x-1,y])
            if x<N-1 and grid[x+1][y] == 0:
                grid[x+1][y] = -1
                Q.append([x+1,y])
            if y>0 and grid[x][y-1] == 0:
                grid[x][y-1] = -1
                Q.append([x,y-1])
            if y<N-1 and grid[x][y+1] == 0:
                grid[x][y+1] = -1
                Q.append([x,y+1])
        
        while Q:
            x,y = Q.pop(0)
            if x>0 and grid[x-1][y] == 0:
                grid[x-1][y] = grid[x][y]-1
                Q.append([x-1,y])
            if x<N-1 and grid[x+1][y] == 0:
                grid[x+1][y] = grid[x][y]-1
                Q.append([x+1,y])
            if y>0 and grid[x][y-1] == 0:
                grid[x][y-1] = grid[x][y]-1
                Q.append([x,y-1])
            if y<N-1 and grid[x][y+1] == 0:
                grid[x][y+1] = grid[x][y]-1
                Q.append([x,y+1])
        
        #print(grid)
        dist = 0
        for i in range(N):
            for j in range(N):
                dist = min(dist,grid[i][j])

        return -dist
        '''
        # print(len(ocean), len(land))
        max_dist = 0
        for o_m,o_n in ocean:
            min_dist = sys.maxsize
            for l_m, l_n in land:
                dist = abs(o_m-l_m) + abs(o_n-l_n)
                min_dist = min(min_dist, dist)
                if min_dist < max_dist:
                    break
            max_dist = max(max_dist, min_dist)
        '''
        return max_dist