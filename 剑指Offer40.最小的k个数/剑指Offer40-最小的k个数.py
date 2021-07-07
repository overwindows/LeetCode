class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        heap = []
        N = len(arr)
        if k >= N:
            return arr
        if k == 0 :
            return []
        for i in range(N):
            if i < k:
                heapq.heappush(heap, -arr[i])
            else:
                if arr[i] < -heap[0]:
                    heapq.heapreplace(heap, -arr[i])
        
        return [-x for x in heap]
            