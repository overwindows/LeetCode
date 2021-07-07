class Solution:
    def minSideJumps(self, obstacles: List[int]) -> int:
        n = len(obstacles)
        
        dp1 = [sys.maxsize] * n
        dp2 = [sys.maxsize] * n
        dp3 = [sys.maxsize] * n

        dp1[0],dp2[0],dp3[0] = 1,0,1

        for i in range(1,n):
            if obstacles[i] == 1:
                dp1[i] = sys.maxsize
                dp2[i] = min(dp2[i-1], dp3[i-1]+1)
                dp3[i] = min(dp3[i-1], dp2[i-1]+1)
            elif obstacles[i] == 2:
                dp2[i] = sys.maxsize
                dp1[i] = min(dp1[i-1], dp3[i-1]+1)
                dp3[i] = min(dp3[i-1], dp1[i-1]+1)
            elif obstacles[i] == 3:
                dp3[i] = sys.maxsize
                dp1[i] = min(dp1[i-1], dp2[i-1]+1)
                dp2[i] = min(dp2[i-1], dp1[i-1]+1)
            else:
                dp1[i] = min(dp1[i-1],dp2[i-1]+1,dp3[i-1]+1)
                dp2[i] = min(dp2[i-1],dp1[i-1]+1,dp3[i-1]+1)
                dp3[i] = min(dp3[i-1], dp2[i-1]+1,dp1[i-1]+1)
        
        return min(dp1[-1],dp2[-1],dp3[-1])
            
            
                
            




            
            

