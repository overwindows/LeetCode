class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        n = len(nums)
        dp=[[[sys.maxsize]*n for _ in range(n)] for _ in range(m+1)]
        
        if m == 1:
            return sum(nums)
        
        # caculate m==1 first.
        for i in range(n):
            for j in range(i,n):
                if i==j:
                    dp[1][i][j] = nums[j]
                else:
                    dp[1][i][j] = dp[1][i][j-1]+nums[j]
        '''
        for k in range(2,m+1):
            for s in range(0,n-k+1):
                for e in range(s+k-1,n):
                    for x in range(s,e):
                        dp[k][s][e] = min(dp[k][s][e], max(dp[1][s][x] ,dp[k-1][x+1][e]))
        '''
        for k in range(2, m+1):
            for i in range(n):
                for j in range(i,n-1):
                    dp[k][i][n-1] = min(dp[k][i][n-1], max(dp[1][i][j], dp[k-1][j+1][n-1]))
                    #print(k,s,e,dp[k][s][e] )
        return dp[m][0][n-1]