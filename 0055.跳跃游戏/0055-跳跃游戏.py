class Solution:
    def canJump(self, nums: List[int]) -> bool:
        N = len(nums)
        if N == 1:
            return True

        max_dist = [0] * (N-1)
        is_zero = False
        for i in range(N-1):
            max_dist[i] = nums[i]+i
            if nums[i] == 0:
                is_zero = True
        if not is_zero:
            return True
        #print(max_dist)

        start = 0
        end = max_dist[0]

        while start <= end:
            if end >= N-1:
                return True
            else:
                end = max(max_dist[start], end)
                start+=1
        return False

'''
[2,3,1,1,4]
[3,2,1,0,4]
[2,3,1,1]
[2,1,1,1,4]
[2,0,1,1,4]
'''