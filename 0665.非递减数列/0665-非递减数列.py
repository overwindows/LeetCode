class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        N = len(nums)
        ix = 0
        for i in range(N-1):
            if nums[i] > nums[i+1]:
              ix = i

        _nums = nums[:]
        del _nums[ix]

        flag = True
        for i in range(N-2):
            if _nums[i] > _nums[i+1]:
                flag = False
                break

        if flag:
            return True
        
        _nums =nums[:]
        del _nums[ix+1]

        for i in range(N-2):
            if _nums[i] > _nums[i+1]:
                return False

        return True 
                      

                
            