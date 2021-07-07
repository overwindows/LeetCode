class Solution:
    def concatenatedBinary(self, n: int) -> int:
        l = []
        for i in range(1,n+1):
            l.append(bin(i)[2:])
        
        return int(''.join(l),2) % (10**9+7)