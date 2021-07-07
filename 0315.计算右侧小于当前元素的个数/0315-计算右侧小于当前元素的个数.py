class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        N = len(nums)
        sorted_nums = []
        counts = []

        if N == 0:
            return counts

        counts.append(0)
        sorted_nums.append(nums[N-1])

        for i in range(1,N):
            tgt = nums[N-1-i]
            
            l = 0
            r = len(sorted_nums)-1

            while l<r:
                m = (l+r)//2
                if sorted_nums[m] >= tgt:
                    r = m-1
                else:
                    l = m+1
            
            if tgt > sorted_nums[l]:
                l = l+1
    
            counts.append(l)
            sorted_nums.insert(l, tgt)
        
        #print(sorted_nums)
        counts.reverse()
        return counts
