class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        _len = 1
        N = len(nums)
        if N == 0:
            return 0

        max_len = 1
        for i in range(1,N):
            if nums[i] > nums[i-1]:
                _len += 1
            else:
                max_len = max(max_len, _len)
                _len = 1
        return max(max_len, _len)