class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        N = len(A)
        if N < 2:
            return True
        
        isMonotonic = 0

        for i in range(N-1):
            j = i+1
            if A[i] == A[j]:
                continue
            if A[i] > A[j]:
                if isMonotonic == 0:
                    isMonotonic = -1
                elif isMonotonic == -1:
                    continue
                else:
                    return False
            else:
                if isMonotonic == 0:
                    isMonotonic = 1
                elif isMonotonic == 1:
                    continue
                else:
                    return False
        
        return True


