class Solution:
    def multiply(self, A: int, B: int) -> int:
        ret = 0
        if A > B:
            a,b = A, B
        else:
            a,b = B, A
        for i in range(b):
            ret += a 
        
        return ret
