class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        maxSum = 0
        N = len(nums)
        dp = [[0]*4 for _ in range(N)]

        if nums[0] % 3 == 1:
            dp[0][1] = nums[0]
        elif nums[0] % 3 == 2:
            dp[0][2] = nums[0]
        else:
            dp[0][3] = nums[0] 

        for i in range(1,N):
            if nums[i] % 3 == 1:
                dp[i][3] = max(dp[i-1][2] + nums[i], dp[i-1][3]) if dp[i-1][2] > 0 else dp[i-1][3]
                dp[i][2] = max(dp[i-1][1] + nums[i], dp[i-1][2]) if dp[i-1][1] > 0 else dp[i-1][2]
                dp[i][1] = max(dp[i-1][3] + nums[i], dp[i-1][1]) 
            elif nums[i] %3 == 2:
                dp[i][3] = max(dp[i-1][1] + nums[i], dp[i-1][3]) if dp[i-1][1] > 0 else dp[i-1][3]
                dp[i][2] = max(dp[i-1][3] + nums[i], dp[i-1][2]) 
                dp[i][1] = max(dp[i-1][2] + nums[i], dp[i-1][1]) if dp[i-1][2] > 0 else dp[i-1][1]
            else:
                dp[i][3] = max(dp[i-1][3] + nums[i], dp[i-1][3]) 
                dp[i][2] = max(dp[i-1][2] + nums[i], dp[i-1][2]) if dp[i-1][2] > 0 else dp[i-1][2]
                dp[i][1] = max(dp[i-1][1] + nums[i], dp[i-1][1]) if dp[i-1][1] > 0 else dp[i-1][1]           

        # print(dp)
        return dp[N-1][3]


"""
[3,6,5,1,8]
[4]
[1,2,3,4,4]
[5,2,2,2]
[4,1,5,3,1]
[13,21,7,27,40,18,37,7,31,5]
"""