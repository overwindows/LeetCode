class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        degree = 0
        d = {}
        for num in nums:
            if num not in d:
                d[num] = 0
            d[num] += 1
            degree = max(degree,d[num])
        
        if degree == 1:
            return 1
        
        for k in d.keys():
            if d[k] != degree:
                d[k] = 0
        
        # print(d)

        N = len(nums)
        if N == 0:
            return 0
        
        dup = {}
        for i in range(N):
            if d[nums[i]]>0:
                if d[nums[i]] == degree:
                    dup[nums[i]] = [i,None]
                elif d[nums[i]] == 1:
                    dup[nums[i]][1] = i
                d[nums[i]] -= 1
            else:
                continue
        shortest = 50001
        for _,v in dup.items():
            start,end = v
            shortest = min(shortest,end-start+1)
        
        return shortest


        
        