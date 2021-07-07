class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        N = len(piles)
        # dp[(i,j)] = max(piles[i]+sum(piles[i+1:j])-dp[(i+1,j)], piles[j]+sum(piles[i:j-1])-dp[(i,j-1)])
        dp = [[0]*N for _ in range(N)]
        c_sum = [0] * (N+1)
        for i in range(N):
            c_sum[i+1] = c_sum[i]+piles[i]

        # print(c_sum)

        for k in range(1,N):
            for i in range(N-k):
                j = i+k
                assert j-i > 0 and j < N
                if k == 1:
                    dp[i][j] = max(piles[i],piles[j])
                else:
                    dp[i][j] = max(piles[i]+(c_sum[j+1]-c_sum[i+1])-dp[i+1][j], piles[j]+(c_sum[j]-c_sum[i])-dp[i][j-1])
        
        return 2*dp[0][N-1]-sum(piles) > 0

