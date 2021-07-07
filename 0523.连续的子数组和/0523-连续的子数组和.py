class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        # if 0 in nums and len(nums) > 1:
        #     return True

        N = len(nums)
        prefix = [0]*N

        for i in range(N):
            if i == 0:
                prefix[i] = nums[i]
            else:
                prefix[i] = prefix[i-1]+nums[i]
                if prefix[i] % k == 0:
                    return True
        
        d = {}
        for i in range(N):
            prefix[i] = prefix[i] % k
            if prefix[i] in d:
                d[prefix[i]].append(i)
            else:
                d[prefix[i]] = [i]

        for k,v in d.items():
            if len(v) == 1:
                continue
            if len(v) > 2:
                return True
            if len(v) == 2:
                a,b = v
                if abs(a-b) > 1:
                    return True
        
        return False
        
"""
[23,2,4,6,7]
6
[23,2,6,4,7]
6
[23,2,6,4,7]
13
[23,2,4,6,6]
7
"""           
        
        

        


        

        

