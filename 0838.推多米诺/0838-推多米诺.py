class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        # find R-L pairs from right to left
        l = list(dominoes)
        r = 10**5+1
        for i in range(len(l)):
            if l[i] == 'R':
                r = i
            if l[i] == 'L' and i > r:
                d = (i-r-1)//2
                for j in range(d):
                    l[r+j+1] = 'R'
                    l[i-j-1] = 'L'
                if (i-r-1)%2:
                    l[r+d+1] = '*'
        
                r = 10**5+1
        
        rt = False
        for x in range(len(l)):
            if l[x] == 'L':
                rt = False
            elif l[x] == 'R':
                rt = True
            elif l[x] == '.':
                if rt:
                    l[x] = 'R'
            else:
                assert l[x] == '*'
        lf = False
        n = len(l)
        for y in range(n):
            if l[n-y-1] == 'L':
                lf = True
            elif l[n-y-1] == 'R':
                lf = False
            elif l[n-y-1] == '.':
                if lf:
                    l[n-y-1] = 'L'
            else:
                assert l[n-y-1] == '*'
            
            
        
        return ''.join(l).replace('*','.')        
                
                
                
        