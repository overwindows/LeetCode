class Solution:
    def hIndex(self, citations: List[int]) -> int:
        if not citations:
            return 0
        
        n = len(citations)
        cnt = [0] * (n + 1)
        for c in citations:
            if c >= n:
                cnt[n] += 1
            else:
                cnt[c] += 1
        
        h_index = 0
        for j in range(n, 0, -1):
            h_index += cnt[j]
            if h_index >= j:
                return j
        
        return 0