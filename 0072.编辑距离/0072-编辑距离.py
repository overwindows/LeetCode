import pprint

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        len1 = len(word1)
        len2 = len(word2)
        '''
        if len1 == 0:
            return len2
        if len2 == 0:
            return len1        
        '''
        mat = [[sys.maxsize] * (len1+1) for _ in range(len2+1)]
        for j in range(len1+1):
            mat[0][j] = j

        for i in range(len2+1):
            mat[i][0] = i

        for i in range(1,len2+1):
            for j in range(1,len1+1):
                mat[i][j] = min(mat[i-1][j-1]+int(word1[j-1]!=word2[i-1]), mat[i-1][j]+1, mat[i][j-1]+1) 
        # pprint.pprint(mat)  

        # Backtracing
        '''
        x = len2
        y = len1

        while x > 0 and y > 0:
            if word1[y-1] == word2[x-1] and mat[x][y] == mat[x-1][y-1]:
                print('[Keep]:{}'.format(word1[y-1]))
                x-=1
                y-=1
            else:
                if mat[x][y] == mat[x-1][y-1]+1:
                    print('[Replace]:{}->{}'.format(word1[y-1], word2[x-1]))
                    x-=1
                    y-=1
                elif mat[x][y] == mat[x-1][y]+1:
                    print('[Insert]:{}->{}'.format(word1[y-1], word2[x-1]))
                    x-=1
                elif mat[x][y] == mat[x][y-1]+1:
                    print('[Delete]:{}->{}'.format(word1[y-1], word2[x-1]))
                    y-=1
        while x > 0:
            print('[Insert]:{}->{}'.format(word1[y-1], word2[x-1]))
            x -= 1

        while y > 0:
            print('[Delete]:{}->{}'.format(word1[y-1], word2[x-1]))
            y-=1
        '''
        return mat[len2][len1]


'''
"ab"
"bc"
"horse"
"ros"
"sea"
"eat"
"a"
"b"
"zoologicoarchaeologist"
"zoogeologist"
"rosettacode"
"raisethysword"
'''