class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        s1_len = len(s1)
        s2_len = len(s2)
        s3_len = len(s3)

        if s1_len+s2_len != s3_len:
            return False
        if s1_len == 0:
            return s2==s3
        if s2_len == 0:
            return s1==s3

        dp = [[False]*(s2_len+1) for _ in range(s1_len+1)]
        dp[0][0] = True
        for i in range(s1_len):
            if s1[i] == s3[i]:
                dp[i+1][0] = True
            else:
                break
        for j in range(s2_len):
            if s2[j] == s3[j]:
                dp[0][j+1] = True
            else:
                break
        
        for i in range(1,s1_len+1):
            for j in range(1,s2_len+1):
                if dp[i-1][j] and s3[i+j-1] == s1[i-1]:
                    dp[i][j] = True
                # print(i,j)
                if dp[i][j-1] and s3[i+j-1] == s2[j-1]:
                    dp[i][j] = True

        # assert dp[2][0] and s3[2] == s2[0]
        # print(dp)
        return dp[s1_len][s2_len] 
                
'''
"aabcc"
"dbbca"
"aadbbcbcac"
"aabcc"
"dbbca"
"aadbbbaccc"
""
""
""
"a"
""
"a"
"db"
"b"
"cbb"
'''
