class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        #(1+N)*N / 2 = candies
        #N*N+N+(1/2)^2 = 2*candies+1/4
        #(N+1/2)^2 = 2*candies+1/4
        n = (2.0*candies+0.25)**0.5-0.5
        N = int(n)
        M = candies-(1+N)*N//2
        #print(N,M)
        ans = [0]*num_people
        num = 1
        for i in range(N):
            ans[i%num_people] += num
            num += 1
        ans[N%num_people] += M
        return ans
