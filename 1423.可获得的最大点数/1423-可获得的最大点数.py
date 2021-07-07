class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        N = len(cardPoints)
        if N <= k:
            return sum(cardPoints)
        
        l,r = [0]*k, [0]*k
        l[0] = cardPoints[0]
        r[0] = cardPoints[-1]
        
        for i in range(1, k):
            l[i] = l[i-1] + cardPoints[i]
        
        for j in range(1, k):
            r[j] = r[j-1] + cardPoints[N-1-j] 
        # print(l,r)
        max_score = max(l[k-1],r[k-1])
        for x in range(k-1):
            max_score = max(max_score, l[x]+r[k-x-2]) 

        return max_score

