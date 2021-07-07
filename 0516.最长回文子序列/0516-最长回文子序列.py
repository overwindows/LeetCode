class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        s = list(s)
        N = len(s)
        if N < 2:
            return N
        dp = [[0]*N for _ in range(N)]
        #max_len = 1
        for i in range(N):
            dp[i][i] = 1
        for j in range(N-1):
            if s[j] == s[j+1]:
                dp[j][j+1] = 2
                #max_len = 2
            else:
                dp[j][j+1] = 1
        #print(N)
        for step in range(2,N):
            for ix in range(N-step):
                if s[ix] == s[ix+step]:
                    dp[ix][ix+step] = dp[ix+1][ix+step-1]+2
                else:
                    dp[ix][ix+step] = max(dp[ix][ix+step-1], dp[ix+1][ix+step])

                #max_len = max(max_len, dp[ix][ix+step])
        return dp[0][N-1]

'''
"bbbab"
"cbbd"
""
"ab"
"a"
"aa"
"euazbipzncptldueeuechubrcourfpftcebikrxhybkymimgvldiwqvkszfycvqyvtiwfckexmowcxztkfyzqovbtmzpxojfofbvwnncajvrvdbvjhcrameamcfmcoxryjukhpljwszknhiypvyskmsujkuggpztltpgoczafmfelahqwjbhxtjmebnymdyxoeodqmvkxittxjnlltmoobsgzdfhismogqfpfhvqnxeuosjqqalvwhsidgiavcatjjgeztrjuoixxxoznklcxolgpuktirmduxdywwlbikaqkqajzbsjvdgjcnbtfksqhquiwnwflkldgdrqrnwmshdpykicozfowmumzeuznolmgjlltypyufpzjpuvucmesnnrwppheizkapovoloneaxpfinaontwtdqsdvzmqlgkdxlbeguackbdkftzbnynmcejtwudocemcfnuzbttcoew"
'''