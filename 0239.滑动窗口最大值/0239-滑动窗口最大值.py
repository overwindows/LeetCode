class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:        
        N = len(nums)
        if k == 0:
            return None
        if k == 1:
            return nums
        if k == N:
            return [max(nums)]
        ret = []

        wnd = []
        max_q = []

        for i in range(k):
            wnd.append(nums[i])
            if max_q:
                while max_q and nums[i] > max_q[-1]:
                    max_q.pop()
                max_q.append(nums[i])
            else:
                max_q.append(nums[i])
        ret.append(max_q[0])
        for i in range(k,N):
            x = wnd.pop(0)
            if x == max_q[0]:
                max_q.pop(0)
            wnd.append(nums[i])
            while max_q and nums[i] > max_q[-1]:
                max_q.pop()
            max_q.append(nums[i])

            ret.append(max_q[0])
        '''
        for i in range(k,N+1):
            part_max = max(nums[i-k:i])
            ret.append(part_max)
        '''
        return ret

