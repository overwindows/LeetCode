class Solution:
    def lastRemaining(self, n: int, m: int) -> int:
        l = [0]*n
        for i in range(n):
            l[i] = i
        ix = 0
        n = len(l)
        while n > 1:
            ix = (ix+m-1)%n
            del l[ix]
            n-=1
        return l[0]

'''
10
7
10
17
5
3
70866
116922
'''


