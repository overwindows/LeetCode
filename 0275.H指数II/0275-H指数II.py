class Solution:
    def hIndex(self, citations: List[int]) -> int:
        N = len(citations)
        if N == 0:
            return 0
        for i in range(1,N+1):
            # print(citations[-i], i)
            if citations[-i] >= i:
                continue
            else:
                return i-1
        return i
         
