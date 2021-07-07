class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        N = len(nums)
        i = 0
        dup = 0
        while i < N:
            if i+1 == nums[i]:
                i += 1
            else:
                x = nums[i]
                if nums[x-1] != x:
                    nums[i] = nums[x-1]
                    nums[x-1] = x
                else:
                    dup = x
                    break

        d = abs(sum(nums) - (1+N)*N//2)

        if sum(nums) < (1+N)*N//2:
            return [dup, dup+d]
        else:
            return [dup, dup-d]
