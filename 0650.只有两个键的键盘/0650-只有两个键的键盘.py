class Solution:
    def minSteps(self, n: int) -> int:
        dp = [0]*(n+1)
        if n == 1:
            return 0
        if n == 2:
            return 2
        dp[1] = 0
        dp[2] = 2
        prim = [2]
        '''
        dp[3] = 1+1+1
        dp[4] = dp[2]+1+1
        dp[6] = dp[3]+1+1
        dp[9] = dp[3]+1+1+1
        '''
        for i in range(3,n+1):
            flag = True
            for p in prim:
                if i % p == 0:
                    flag = False
                    x = i//p
                    # print(i,x,p)
                    dp[i] = dp[x]+p
                    # print(dp[i])
                    break
            if flag:
                prim.append(i)
                dp[i] = i
        
        return dp[n]

"""
1
2
3
4
5
6
7
8
9
10
100
1000
"""
