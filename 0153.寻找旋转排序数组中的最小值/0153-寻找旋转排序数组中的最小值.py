class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return None
        if len(nums) == 1:
            return nums[0]
        
        st = 0
        ed = len(nums) - 1

        while st < ed:
            mid = (st+ed)//2
            if nums[mid] > nums[ed]:
                st = mid+1
            else:
                ed = mid
        
        return nums[st]