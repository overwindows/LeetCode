class Solution:
    def massage(self, nums: List[int]) -> int:
        N = len(nums)
        if N < 1:
            return 0
        dp = [0] * N
        for i in range(N):
            dp[i] = nums[i]
        
        for i in range(N):
            if i > 1:
                dp[i] = max(dp[i], dp[i-2]+nums[i])
            if i > 2:
                dp[i] = max(dp[i], dp[i-3]+nums[i])

        return max(dp[N-1],dp[N-2])

'''
[1,2,3,1]
[2,7,9,3,1]
[2,1,4,5,3,1,1,3]
[1]
[]
[3,1]
[2,1,1,2]
'''