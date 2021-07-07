class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        N = len(nums)
        start = 0
        end = N-1
        
        cnt = 0
        while start < end:
            if nums[start] + nums[end] == k:
                cnt += 1
                start += 1
                end -= 1
            elif nums[start] + nums[end] < k:
                start += 1
            else:
                end -= 1
        return cnt            