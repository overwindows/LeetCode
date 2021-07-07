class Solution:
    def countBits(self, num: int) -> List[int]:
        
        # bits = [0,1,1,2,1,2]
        bits = [0] * (num+1)

        for n in range(1,num+1):
            if n%2:
                bits[n] = bits[n-1]+1
            else:
                bits[n] = bits[n//2]
        
        return bits
