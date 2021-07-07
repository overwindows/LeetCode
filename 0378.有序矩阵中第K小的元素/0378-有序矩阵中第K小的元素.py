class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        if n == 0:
            return 0
        if k == 1:
            return matrix[0][0]
        if k == n*n:
            return matrix[n-1][n-1]
        heap = []
        heapq.heappush(heap, (matrix[0][0],0,0))
        #print(heap)
        for _ in range(k-1):
            s,i,j = heapq.heappop(heap)
            if j+1 < n and matrix[i][j+1] != sys.maxsize:
                heapq.heappush(heap, (matrix[i][j+1],i,j+1))
                matrix[i][j+1] = sys.maxsize
            if i+1 < n and matrix[i+1][j] != sys.maxsize:
                heapq.heappush(heap, (matrix[i+1][j],i+1,j))
                matrix[i+1][j] = sys.maxsize
            #print(heap)
        
        smallest,_,_ = heapq.heappop(heap)

        return smallest
'''
[[1,5,9],[10,11,13],[12,13,15]]
8
[[1,3,5],[6,7,12],[11,14,14]]
6
[[1,2],[1,3]]
2
'''