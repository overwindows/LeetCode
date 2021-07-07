class Solution:
    def findSubstringInWraproundString(self, p: str) -> int:
        p_len = len(p)
        # if p_len < 1:
        #     return 0
        dp = [1]*p_len

        for i in range(1,p_len):
            if p[i-1] == 'z' and p[i] == 'a':
                dp[i] = dp[i-1]+dp[i]
            
            if ord(p[i]) - ord(p[i-1]) == 1:
                dp[i] = dp[i-1]+dp[i]

        pairs = {}
        for i in range(p_len):
            if p[i] not in pairs:
                pairs[p[i]] = dp[i]
            else:
                pairs[p[i]] = max(dp[i], pairs[p[i]])

        cnt = 0
        
        for k,v in pairs.items():
            cnt += v

        return cnt            