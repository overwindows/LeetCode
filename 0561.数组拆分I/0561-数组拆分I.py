class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        min_sum = 0
        N = len(nums)
        for i in range(0,N-1,2):
            min_sum += nums[i]

        return min_sum