class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        a = []
        prev = None
        n = len(s)
        for i in range(n):
            if not prev:
                a.append([i,1])
                prev = s[i]
            else:
                if prev == s[i]:
                    a[-1][1] += 1
                else:
                    if a[-1][1] < 3:
                        a.pop()
                    a.append([i,1])
                    prev = s[i]
        
        if a[-1][1] < 3:
            a.pop()
        for i in range(len(a)):
            a[i][1] = a[i][0]+a[i][1]-1
        a.sort()
        return a
            