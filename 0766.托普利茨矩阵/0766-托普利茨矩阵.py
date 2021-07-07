class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        N = len(matrix)
        M = len(matrix[0])

        # row[0]
        for m in range(M-1):
            r = 0
            c = m
            x = matrix[r][c]

            r += 1
            c += 1
            flag = True
            while r < N and c < M:
                if x != matrix[r][c]:
                    flag = False
                    break
                else:
                    r+=1
                    c+=1
            if not flag:
                return False
        
        for n in range(1,N-1):
            c = 0
            r = n

            x = matrix[r][c]
            r += 1
            c += 1
            flag = True
            while r < N and c < M:
                if x != matrix[r][c]:
                    flag = False
                    break
                else:
                    r+=1
                    c+=1
            if not flag:
                return False


            
        return True