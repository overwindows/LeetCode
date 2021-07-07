class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)
        m_val = [[0]*k for _ in range(n)]
        
        for kk in range(k):
            for nn in range(n-kk):
                if kk == 0:
                    m_val[nn][0] = arr[nn]
                else:
                    m_val[nn][kk] = max(m_val[nn][kk-1], arr[nn+kk])
        # print(m_val)

        dp = [0]*n
        dp[0] = arr[0]
        for i in range(1,n):
            dp[i] = dp[i-1]+arr[i]
        # print(dp)
        
        for nn in range(n):
            for kk in range(k):
                if nn-kk > -1:
                    dp[nn] = max(dp[nn], m_val[nn-kk][kk]*(kk+1))
                if nn-kk > 0:
                    dp[nn] = max(dp[nn], dp[nn-kk-1] + m_val[nn-kk][kk]*(kk+1))
                

        return dp[-1]
"""
[1,15,7,9,2,5,10]
3
[1,15,7,9,2,5,10]
4
[1,4,1,5,7,3,6,1,9,9,3]
4
[1,4,1,5,7,3,6,1,9,9,3]
2
[1,4,1,5,7,3,6,1,9,9,3]
3
[1,4,1,5,7,3,6,1,9,9,3]
5
[1,4,1,5,7,3,6,1,9,9,3]
7
[1,4,1,5,7,3,6,1,9,9,3]
1
[1,2,3,4,5,6,7,8,9,10]
1
[8,5,7]
3
[7,2]
1
[10,9,3,2]
2
"""