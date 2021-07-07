class Solution:
    def convertToTitle(self, n: int) -> str:
        alphabets = {}

        for i in range(1,27):
            alphabets[i] = chr(64+i)
        
        res = []
        alphabets[0] = 'Z'

        while n > 26:
            res.append(alphabets[n%26])
            if n%26:
                n = n // 26
            else:
                n = n // 26 -1
        
        res.append(alphabets[n])
        res = res[::-1]
        return ''.join(res)

