class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        M = len(matrix)
        N = len(matrix[0])

        i = 0
        j = M-1
        mid = 0
        while i <= j:
            mid = (i+j)//2
            if matrix[mid][0] < target:
                i = mid+1
            elif matrix[mid][0] > target:
                j = mid-1
            else:
                break
        
        if matrix[mid][0] == target:
            return True
        elif matrix[mid][0] < target:
            m = mid
        else:
            m = mid-1
            if m < 0:
                return False

        i = 0
        j = N-1

        while i <= j:
            mid = (i+j)//2
            if matrix[m][mid] < target:
                i = mid+1
            elif matrix[m][mid] > target:
                j = mid-1
            else:
                return True
        return False
