class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # in-place merge sort.
        _nums = nums[:]
        _nums.sort()
        N = len(_nums)
        mid = N//2+N%2
        l = _nums[:mid]
        r = _nums[mid:]

        l.reverse()
        r.reverse()

        l_ix = 0
        r_ix = 0

        for i in range(0,N,2):
            nums[i] = l[l_ix]
            l_ix += 1

        for j in range(1,N,2):
            nums[j] = r[r_ix]
            r_ix += 1
        

        
"""
[4,5,5,6]
[1,5,1,1,6,4]
[1, 3, 2, 2, 3, 1]
[1,1,1,2,2]
[1,1,1,1,2,2,2]
[2,2,1,1,1]
"""