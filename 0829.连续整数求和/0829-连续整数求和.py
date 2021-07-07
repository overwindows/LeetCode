class Solution:
    def consecutiveNumbersSum(self, N: int) -> int:
        consecutive = 1
        
        m = int((2*N)**0.5)+1
        
        for i in range(2,m):
            if 2*N % i == 0:
                # print(i)
                if (2*N // i - i+1) % 2 == 0:
                    consecutive += 1
        
        return consecutive
        