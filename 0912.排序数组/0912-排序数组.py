class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def qsort(ary, st, ed):
            if ed-st < 1:
                return
            
            start = st
            end = ed
            
            pivot = ary[st] 
            while st < ed:
                while st < ed and ary[ed] >= pivot:
                    ed -= 1
                if ary[ed] < pivot:
                    ary[st] = ary[ed]
                    st +=1
                else:
                    assert st == ed
                    break
                
                while st < ed and ary[st] <= pivot:
                    st += 1
                if ary[st] > pivot:
                    ary[ed] = ary[st]
                    ed -= 1
                else:
                    assert st == ed
                    break
            
            ary[st] = pivot

            qsort(ary,start,st-1)
            qsort(ary,st+1,end)

        N = len(nums)
        if N < 2:
            return nums
        qsort(nums,0,N-1)

        return nums
'''
[5,2,3,1]
[5,1,1,2,0,0]
'''