class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        dp = [[[0]*maxMove for _ in range(n)] for _ in range(m)]
        for N in range(maxMove):
            for mm in range(m):
                for nn in range(n):
                    if N == 0:
                        if mm == 0:
                            dp[mm][nn][N] += 1
                        if nn == 0:
                            dp[mm][nn][N] += 1
                        if mm == m-1:
                            dp[mm][nn][N] += 1
                        if nn == n-1:
                            dp[mm][nn][N] += 1
                    else:
                        assert N > 0
                        if mm > 0:
                            dp[mm][nn][N] += dp[mm-1][nn][N-1]
                        if mm+1<m:
                            dp[mm][nn][N] += dp[mm+1][nn][N-1]
                        if nn+1<n:
                            dp[mm][nn][N] += dp[mm][nn+1][N-1]
                        if nn > 0:
                            dp[mm][nn][N] += dp[mm][nn-1][N-1]
        return sum(dp[startRow][startColumn]) % (10**9+7)