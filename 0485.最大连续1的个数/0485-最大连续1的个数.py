class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        N = len(nums)
        if N < 1:
            return 0
        max_ones = nums[0]
        for i in range(1,N):
            if nums[i] == 1:
                nums[i] += nums[i-1]
                max_ones = max(nums[i], max_ones)
        return max_ones