class Solution:


    def reversePairs(self, nums: List[int]) -> int:
        '''
        N = len(nums)
        cnt = 0
        for i in range(N-1):
            for j in range(N-i-1):
                if nums[j] > nums[j+1]:
                    nums[j],nums[j+1] = nums[j+1],nums[j]
                    cnt += 1
        '''
        def mergeSort(nums: List[int]):
            N = len(nums)
            if N <= 1:
                return 0, nums[:]
            if N == 2:
                if nums[0] > nums[1]:
                    nums[0],nums[1] = nums[1], nums[0]
                    return 1, nums[:]
                else:
                    return 0, nums[:]
            
            mid = N // 2
            cnt_left, nums_left = mergeSort(nums[:mid])
            cnt_right, nums_right = mergeSort(nums[mid:])

            #merge
            left_n = len(nums_left)
            assert left_n == mid
            right_n = len(nums_right)
            merge = []
            cnt,l,r = 0,0,0
            while l < left_n and r < right_n:                
                if nums_left[l] <= nums_right[r]:
                    merge.append(nums_left[l])
                    l += 1
                else:
                    merge.append(nums_right[r])
                    r += 1
                    #print(left_n-l)
                    cnt += (left_n - l)
            
            while l < left_n:
                merge.append(nums_left[l])
                l+=1
            while r < right_n:
                merge.append(nums_right[r])
                r += 1

            #print(cnt,cnt_left, cnt_right)

            return cnt+cnt_left+cnt_right, merge
        cnt, _ = mergeSort(nums)
        return cnt



'''
[7,5,6,4]
[7,6,5,4]
[]
[1]
[1,3,2,3,1]
'''