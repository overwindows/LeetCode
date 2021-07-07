import pprint
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        s_len = len(s)
        t_len = len(t)

        if s_len == 0:
            return 0
        if t_len ==0:
            return 0

        mat = [[0]*t_len for _ in range(s_len)]

        for i in range(s_len):
            for j in range(t_len):
                if s[i] == t[j] and j<=i:
                    mat[i][j] = 1
        
        #pprint.pprint(mat)

        for n in range(t_len):
            for m in range(s_len):
                if mat[m][n] and m>0 and n>0:
                    mat[m][n] = mat[m-1][n-1]
            
            for m in range(s_len):
                if m>0:       
                    mat[m][n] += mat[m-1][n]

        #pprint.pprint(mat)

        return mat[-1][-1]
'''
"rabbbit"
"rabbit"
"babgbag"
"bag"
""
"a"
'''