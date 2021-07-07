class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort()
        pairs_len = len(pairs)

        dp = [1]*pairs_len

        for i in range(1,pairs_len):
            for j in range(i):
                if pairs[i][0] > pairs[j][1]:
                    dp[i] = max(dp[i],dp[j]+1)
        return dp[-1]
