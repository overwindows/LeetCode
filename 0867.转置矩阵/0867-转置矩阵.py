class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        M = len(A)
        if M == 0:
            return []
        N = len(A[0])

        B = [[0]*M for _ in range(N)]

        for i in range(M):
            for j in range(N):
                B[j][i] = A[i][j]
        
        return B