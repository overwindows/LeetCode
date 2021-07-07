class Solution:
    def candy(self, ratings: List[int]) -> int:
        N = len(ratings)
        fwd = [1] * N
        bwd = [1] * N

        # forward
        for i in range(1,N):
            if ratings[i] > ratings[i-1]:
                fwd[i] = fwd[i-1]+1

        for j in range(1,N):
            #print(ratings[N-i-1], ratings[N-i])
            if ratings[N-j-1] > ratings[N-j]:
                bwd[N-j-1] = bwd[N-j] + 1

        # print(fwd)
        # print(bwd)
        
        cnt = 0
        for k in range(N):
            cnt += max(fwd[k], bwd[k])

        return cnt                

'''
[1,0,2]
[1,2,2]
[1,3,2,2,1]
'''