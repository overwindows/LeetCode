class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        col = set()
        row = set()

        N = len(matrix)
        M = len(matrix[0])

        for n in range(N):
            for m in range(M):
                if matrix[n][m] == 0:
                    row.add(n)
                    col.add(m)
        
        for n in range(N):
            for m in range(M):
                if n in row or m in col:
                    matrix[n][m] = 0

                    
                    