class Solution:
    def minIncrementForUnique(self, A: List[int]) -> int:
        d = {}
        s = set()
        set_A = set(A)
        slot = []
        cnt =0
        Magic = 80000
        for n in A:
            if n not in d:
                d[n] = 0
            d[n] += 1
            if d[n] > 1:
                s.add(n)
        #print(s)
        for i in range(Magic):
            if i not in set_A:
                slot.append(i)
        slot.sort()
        l = list(s)
        l.sort()
        while l:
            x = l.pop(0)
            while d[x] > 1:
                while slot:
                    y = slot.pop(0)
                    assert x != y
                    if y > x:
                        cnt += y-x
                        break
                d[x] -= 1
        return cnt
'''
[1,2,2]
[3,2,1,2,1,7]
[]
[1]
[2,2,2,1]
[2,1,1,1]
''' 